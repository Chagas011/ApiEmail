import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
pessoas = pd.read_excel('clientes.xlsx')

for index, pessoa in pessoas.iterrows():
    print(pessoa['email'])
    msg = MIMEMultipart("alternative")
    msg['Subject'] = 'BLOQUEIO TEMPORARIO DE CONTA-PROTOCOLO: 926910498'
    msg['From'] = 'nu_central@hotmail.com'
    msg['To'] = pessoa['email']
    msg.add_header('Reply-To', 'nu_central@hotmail.com')
    msg.attach(
        MIMEText(f'Olá, Cliente Nu {pessoa['email']}'))
    message = f"""
    <html>
<body>
<h1 style="color: purple; text-align: center;">Ola {pessoa['email']} Transferência bloqueada por segurança </h1>
<p style="font-size: 20px; text-align: center;">Nosso sistema detectou algumas <span style="font-weight: 600;"> transações incomuns em sua conta e por
esse motivo sua conta foi bloqueada temporáriamente por motivos de segurança juntamente com os valores respectivos. </span>
</p>
<div style="text-align: center;">
<h3>Transferência PIX (Bloqueada por segurança)</h3>

<span style="font-weight: 600;">Valor:</span>
<P style="font-weight: 600;">R$ 3.789,90 </P>
<span style="font-weight: 600;">nome:</span>
<P style="font-weight: 600;">Paulo Henrique Souza</P>
<span style="font-weight: 600;">banco:</span>
<P style="font-weight: 600;">Nubank</P>
</div>
<h3 style="text-align: center;">
Ligue para <span style="font-weight: 600; font-size: 30px; text-align: center;">4003-4046</span> e cancele está transação
</h3>

<div style="align-items: center; text-align: center;">
<a href="tel:+5511954584787" style="height: 50px; width: 250px; background-color: purple; color: white;
text-align: center; border-radius: 30px;cursor: pointer; text-decoration: none">Ligar
Para suporte </a>
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
