import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd


pessoas = pd.read_excel('clientes.xlsx')

for index, pessoa in pessoas.iterrows():
    print(pessoa['email'])
    msg = MIMEMultipart("alternative")
    msg['Subject'] = 'relatorio de vendas'
    msg['From'] = 'SEU EMAIL OUTLOOK OU HOTMAIL'
    msg['To'] = pessoa['email']
    msg.add_header('Reply-To', 'SEU EMAIL OUTLOOK OU HOTMAIL')
    message = """
    <html>
<body>
<h1 style="color: purple; text-align: center;">Transferência bloqueada por segurança </h1>
<p style="font-size: 20px; text-align: center;">Notamos algumas transações incomuns em sua conta e por este motivo sua
conta foi bloqueada
</p>
<div style="text-align: center;">
<h3>Transferência PIX bloqueada</h3>

<span style="font-weight: 600;">Valor:</span>
<P style="font-weight: 300;">R$ 1.979,42 </P>
<span style="font-weight: 600;">nome:</span>
<P style="font-weight: 300;">BANCO ITAU - 341 AG: 6182 </P>
<span style="font-weight: 600;">banco:</span>
<P style="font-weight: 300;">Victor Pereira de Souza </P>
</div>
<h3>
Ligue para <span style="font-weight: 600; font-size: 30px;">4003-4046</span> e cancele esta transacao caso contrario
sua
conta sera bloqueada permanentemente e excluida apos 30 dias por nao cumprir nossos termos
</h3>

<div style="align-items: center; text-align: center;">
<button
style="height: 50px; width: 150px; background-color: purple; color: white; text-align: center; border-radius: 30px;">Ligar
Para suporte</button>
</div>
</body>

</html>


    """
    msg.attach(MIMEText(
        message, 'html', 'utf-8'))
    file_name = 'teste.txt'
    caminho_arquivo = 'teste.txt'
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
                 'SUA SENHA DO EMAIL')
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
