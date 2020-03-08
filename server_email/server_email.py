import redis
import json
import os
from time import sleep
from random import randint

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

if __name__ == '__main__':
    redis_host = os.getenv('REDIS_HOST', 'queue')
    email = os.getenv('EMAIL', 'NÃO INFORMADO')
    password = os.getenv('PASSWORD', 'NÃO INFORMADO')
    servidor_email = os.getenv('EMAIL_SERVER', 'NÃO INFORMADO')
    porta_servidor_email = os.getenv('PORT_EMAIL_SERVER', 'NÃO INFORMADA')
    r = redis.Redis(host=redis_host, port=6379, db=0)
    print('Aguardando mensagens!!!')
    while True:
        mensagem = json.loads(r.blpop('sender')[1])

        if email == 'NÃO INFORMADO' or email == 'conta_email@dominio.com.br' \
        or password == 'senha_conta_email' or password == 'NÃO INFORMADO'  \
        or servidor_email == 'NÃO INFORMADO' \
        or porta_servidor_email == 'NÃO INFORMADA':
            # Simulando de envio de e-mail
            print('Enviando a mensagem: ', mensagem['assunto'])
            sleep(randint(15, 45))
            print('Mensagem', mensagem['assunto'], 'enviada')
        else:
            # Envio de Email
            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = email
            msg['Subject'] = mensagem['assunto']
            msg.attach(MIMEText(mensagem['mensagem'], 'plain'))

            print('AUTENTICAÇÃO DE EMAIL')
            server = smtplib.SMTP('{0}: {1}'.format(
                servidor_email, porta_servidor_email))
            server.starttls()
            server.login(msg['From'], password)
            print('EMAIL AUTENTICADO')
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            print("Email enviado com sucesso para: ", (msg['To']))
            server.quit()
