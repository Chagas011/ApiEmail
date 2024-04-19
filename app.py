import requests

pessoas = [
    {'nome': 'Thiagao', 'email': 'washington_867@live.com'},
    {'nome': 'Thiagao', 'email': 'washington_867@live.com'},
]

for cliente in pessoas:
    # Substitua 'sua_chave_de_api_aqui' pela sua chave de API do Elastic Email
    api_key = 'F1946AA07C48B177881E520EE40FF727627F'
    from_email = 'washington.chagas.9@hotmail.com'
    to_email = cliente['email']
    subject = 'relatorio de venda'
    # Corrigido aqui
    content = f'Ola {cliente["nome"]} você recebeu um email importante'

    url = 'https://api.elasticemail.com/v2/email/send'
    payload = {
        'apikey': api_key,
        'from': from_email,
        'to': to_email,
        'subject': subject,
        'body_html': content
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(f'E-mail enviado com sucesso para {to_email}!')
    else:
        print('Erro ao enviar e-mail:', response.text)
