import qrcode

# Mensagem que será exibida quando o QR code for lido
mensagem = "Valeu por tudo!!! Ass Budah"

# Crie o QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(mensagem)
qr.make(fit=True)

# Crie uma imagem do QR code
img = qr.make_image(fill_color="black", back_color="white")

# Salve o QR code em um arquivo
img.save("qr_code.png")
