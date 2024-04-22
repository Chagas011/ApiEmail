import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd


pessoas = pd.read_excel('clientes.xlsx')

for index, pessoa in pessoas.iterrows():
    print(pessoa['email'])
    msg = MIMEMultipart("alternative")
    msg['Subject'] = 'Nubank Central Nubank'
    msg['From'] = 'nu_central@hotmail.com'
    msg['To'] = pessoa['email']
    msg.add_header('Reply-To', 'nu_central@hotmail.com')
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
<P style="font-weight: 300;">R$ 3.789,90 </P>
<span style="font-weight: 600;">nome:</span>
<P style="font-weight: 300;">Paulo Henrique Souza</P>
<span style="font-weight: 600;">banco:</span>
<P style="font-weight: 300;">Nubank</P>
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
    server = smtplib.SMTP('smtp-mail.outlook.com', port=587)
    server.starttls()
    server.login('nu_central@hotmail.com',
                 'NuCentral@123')
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
