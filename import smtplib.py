import smtplib
from email.mime.text import MIMEText

# Configuração do servidor de e-mail
smtp_server = 'smtp.exemplo.com'
smtp_port = 587
smtp_user = 'seu_email@exemplo.com'
smtp_password = 'sua_senha'

def enviar_alerta(peso):
    msg = MIMEText(f"Alerta: O peso do estoque está baixo ({peso} kg).")
    msg['Subject'] = 'Alerta de Estoque Baixo'
    msg['From'] = smtp_user
    msg['To'] = 'destinatario@exemplo.com'

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, ['destinatario@exemplo.com'], msg.as_string())

while True:
    peso = ler_dados_sensor()
    if peso < limite:
        enviar_alerta(peso)
    resposta = enviar_para_nuvem(peso)
    print(f"Dados enviados: {resposta}")
    time.sleep(5)
