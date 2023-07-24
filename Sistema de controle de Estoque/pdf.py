import aspose.pdf as ap

# Inicializar objeto de documento
document = ap.Document()

# Adicionar Página
page = document.pages.add()

# Inicializar objeto textfragment
text_fragment = ap.text.TextFragment("Hello,world!")
text_fragment.config(CENTER)

# Adicionar fragmento de texto à nova página
page.paragraphs.add(text_fragment)

# Salvar PDF atualizado
document.save("output.pdf")

