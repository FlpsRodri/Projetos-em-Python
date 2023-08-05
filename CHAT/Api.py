from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime, timedelta
#API para comunicação entre chat

app = Flask(__name__)

def create_tables():
    conn = sqlite3.connect('messages.sql')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT, token TEXT, user TEXT, cpf TEXT, recipient TEXT, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    c.execute('''CREATE TABLE IF NOT EXISTS authorized_users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, token TEXT, user TEXT, cpf TEXT)''')
    conn.commit()
    conn.close()

def is_user_authorized(token, user, cpf):
    conn = sqlite3.connect('messages.sql')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM authorized_users WHERE token = ? AND user = ? AND cpf = ?", (token, user, cpf))
    count = c.fetchone()[0]
    conn.close()
    return count > 0

def delete_old_messages():
    conn = sqlite3.connect('messages.sql')
    c = conn.cursor()
    
    one_month_ago = datetime.now() - timedelta(days=30)
    c.execute("DELETE FROM messages WHERE timestamp < ?", (one_month_ago,))
    
    conn.commit()
    conn.close()

@app.route('/add_message', methods=['POST'])
def add_message():
    content = request.json.get('content')
    token = request.json.get('token')
    user = request.json.get('user')
    cpf = request.json.get('cpf')
    recipient = request.json.get('recipient')

    if content and token and user and cpf and recipient and is_user_authorized(token, user, cpf):
        conn = sqlite3.connect('messages.sql')
        c = conn.cursor()
        c.execute("INSERT INTO messages (content, token, user, cpf, recipient) VALUES (?, ?, ?, ?, ?)",
                  (content, token, user, cpf, recipient))
        conn.commit()
        conn.close()
        delete_old_messages()  # Exclui mensagens antigas
        return jsonify({'message': 'Mensagem arquivada com sucesso!'}), 201
    else:
        return jsonify({'error': 'Dados inválidos ou usuário não autorizado'}), 400

@app.route('/get_messages', methods=['GET'])
def get_messages():
    token = request.args.get('token')
    user = request.args.get('user')
    cpf = request.args.get('cpf')
    recipient = request.args.get('recipient')

    if token and user and cpf and recipient and is_user_authorized(token, user, cpf):
        conn = sqlite3.connect('messages.sql')
        c = conn.cursor()
        c.execute("SELECT * FROM messages WHERE recipient = ?", (recipient,))
        messages = [{'id': row[0], 'content': row[1]} for row in c.fetchall()]
        conn.close()
        return jsonify(messages), 200
    else:
        return jsonify({'error': 'Dados inválidos ou usuário não autorizado'}), 400

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
