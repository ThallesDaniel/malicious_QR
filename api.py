from flask import Flask, request, jsonify
import socket
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/api/capturar', methods=['POST'])
def capturar_informacoes():
    try:
        # Captura o IP da pessoa que leu o QR code
        ip = request.remote_addr

        # Captura o nome do aparelho
        nome_aparelho = socket.gethostname()

        # Enviar as informações por e-mail
        enviar_email(ip, nome_aparelho)

        return jsonify({"mensagem": "Informações capturadas e e-mail enviado com sucesso!"})
    except Exception as e:
        return jsonify({"erro": str(e)})

def enviar_email(ip, nome_aparelho):
    try:
        # Configurar a conexão SMTP
        smtp_server = 'smtp.gmail.com'  # Substitua pelo servidor SMTP do seu provedor
        smtp_port = 587  # Porta SMTP do seu provedor (geralmente 587 ou 465)
        smtp_username = 'teste@teste.com'  # Seu endereço de e-mail institucional
        smtp_password = 'UVB76Ckd3301'  # Sua senha de e-mail

        destinatario = 'teste@gmail.com'  # Substitua pelo endereço de e-mail do destinatário

        # Configurar a conexão SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Criar uma mensagem de e-mail
        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = destinatario
        msg['Subject'] = 'Informações do QR Code Lido'

        # Corpo do e-mail
        corpo_email = f"IP: {ip}\nNome do Aparelho: {nome_aparelho}"
        msg.attach(MIMEText(corpo_email, 'plain'))

        # Enviar o e-mail
        server.sendmail(smtp_username, destinatario, msg.as_string())

        # Encerrar a conexão SMTP
        server.quit()

        return "E-mail enviado com sucesso!"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
