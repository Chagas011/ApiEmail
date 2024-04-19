import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

pessoas = [
    {'nome': 'NOME DOS DESTINATARIOS', 'email': 'EMAIL DOS DESTINATARIOS'},
    {'nome': 'NOME DOS DESTINATARIOS', 'email': 'EMAIL DOS DESTINATARIOS'},
    
]

for pessoa in pessoas:
    msg = MIMEMultipart()
    msg['Subject'] = 'relatorio de vendas'
    msg['From'] = 'SEU EMAIL OUTLOOK OU HOTMAIL'
    msg['To'] = pessoa['email']
    msg.add_header('Reply-To', 'SEU EMAIL OUTLOOK OU HOTMAIL')
    message = f'Ola {pessoa['nome']} vc recebeu um email importante'
    msg.attach(MIMEText(
        message, '\nEste e-mail será entregue na caixa de entrada do destinatário.'))
    file_name = 'teste.txt' # NOME DO ARQUIVO Q QUER ENVIAR EM ANEXO
    caminho_arquivo = 'teste.txt' # CAMINHO DO ARQUIVO/ DEIXAR ARQUIVO NO MESMO NIVEL Q O APP
    with open(caminho_arquivo, 'rb') as anexo:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(anexo.read())

    encoders.encode_base64(part)
    part.add_header(
        'Content-Disposition',
        f'attachment; filename= {file_name}',
    )
    msg.attach(part)
    server = smtplib.SMTP('smtp-mail.outlook.com', port=587)
    server.starttls()
    server.login('SEU EMAIL OUTLOOK OU HOTMAIL',
                 'SUA SENHA')
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
