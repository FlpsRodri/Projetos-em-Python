import qrcode

def q
qr = qr.QRCode(
	version=1,
	error_correction=qrcode.constants.ERROR_CORRECT_L,
	box_size=10,
	border=4)

qr.add_data('https://programadorviking.com.br')
qr.make(fit=True)

imagem = qr.make_image(fill_color='black',back_color='white')
imagem.save('qrcode-site.png')


