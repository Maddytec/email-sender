
# Email Sender

Microservices utilizando docker compose para envio de emails com frontend em Bootstrap, backend em Python, banco PostrgreSQL e fila com Redis.

![Figura 1 - Container](image/containers.png)
<br>Figura 1 - Containers com suas respectivas tecnologias e conexões de rede

## Faça agora, por que na minha máquina funciona ;)
1. [Baixar projeto](#1-baixar-projeto)
<br>1.1 [Apenas simular o envio de E-mail]( #21-para-apenas-simular-o-envio-de-e-mail-siga-para-passo-23)
<br>1.2 [Simular envio de email]( #12-para-envio-de-emails-é-necessário-a-configuração-das-variáveis-de-nosso-servidor-de-e-mail-server_email)
<br>2.3 [Simular envio de email]( #21-para-apenas-simular-o-envio-de-e-mail-siga-para-passo-23)
2. [Inicializando os serviços](#2-inicializando-os-serviços)
3. [Como testar o projeto?](#3-como-testar-o-projeto)
<br>3.1 [Tela de envio de mensagens](#31---tela-de-envio-de-mensagens)
<br>3.2 [Consulta das mensagens enviadas no item anterior e persistidas no banco de dados PostgreSQL](#32-consulta-das-mensagens-enviadas-no-item-anterior-e-persistidas-no-banco-de-dados-postgresql)
<br>3.3 [Replicando servidor de emails](#33-replicando-servidor-de-emails)
<br>3.4 [Log do consumo da fila Redis](#34-log-do-consumo-da-fila-redis)
4. [Remover os serviços](#4-remover-os-servi%C3%A7os)
5. [Licença](#5-licença)


Requisitos necessários para prosseguir :
*  [Git](https://git-scm.com/downloads)
*  [Docker](https://docs.docker.com/get-docker/)
*  [Docker Compose](https://docs.docker.com/compose/install/)

## 1. Baixar projeto
- No console do seu sistema operacional execute o comando: 
<br>`$ git clone https://github.com/Maddytec/email-sender.git`
### 1.1 Apenas simular o envio de E-mail siga para passo 2

### 1.2 Configuração do Servidor de Email server_email  
- Para envio de emails é necessário a configuração das variáveis de nosso servidor de E-mail. Desta forma, substitua os valores atribuídos as variáveis EMAIL, PASSWORD, EMAIL_SERVER e PORT_EMAIL_SERVER  encontradas no arquivo Docker-compose.override.yml pelos respectivos valores do servidor de E-mail de sua escolha.
-  Caso o servidor de E-mail escolhido seja Gmail, o Google, à princípio, não vai permitir realizar o login, Para resolver isso, vá em [https://www.google.com/settings/security/lesssecureapps](https://www.google.com/settings/security/lesssecureapps) enquanto estiver logado na sua conta Google, e mude para "ON" a oção de "Allow less secure apps". Não esqueça, no final dos teste desabilite novamente o recurso.
 

## 2. Inicializando os serviços
 - Comandos para iniciar os serviços:
<br>`$ cd email-sender`
<br> `$ docker-compose up -d`

- Comando para listar os serviços:
<br>`$ docker-compose ps`

![Figura 2 - Retorno do comando docker-compose ps](image/ps.png)
<br>Figura 2 - Retorno do comando docker-compose ps

## 3. Como testar o projeto?

Após executar o item 2:
  
### 3.1 Tela de envio de mensagens

 - Acessar a URL: [http://localhost](http://localhost) para visualizar a pagina disponibilizada referente ao frontend

![Figura 3 - Tela de envio de mensagem](image/mensagem.png)
<br>Figura 3 - Tela de envio de  mensagens
  
### 3.2 Consulta das mensagens enviadas no item anterior e persistidas no banco de dados PostgreSQL
- Comando para cosultar as mensagens da tabela emails no banco email_sender e com usuario postgres  
`$ docker-compose exec db psql -U postgres -d email_sender -c "select * from emails"`

![Figura 4 - Mensagens persistidas](image/select.png)
<br>Figura 4 - Mensagens persistidas

## 3.3 Replicando servidor de emails
- Comando para replicar o serviço de emails:
<br>`$ docker-compose up -d --scale server_email=3`

- Comando para verificar os serviços disponíveis
<br>`docker-compose ps`    

![Figura 5 - Retorno do comando docker-compose ps](image/emails.png)
<br>Figura 5 - Retorno do comando docker-compose ps

## 3.4 Log do consumo da fila Redis
- Comando para acompanhar o log dos servidores de emails consumindo a fila
<br>`$ docker-compose logs -f -t server_email` 

![Figura 6 - Retorno do comando](image/log.png)
<br>Figura 6 - Exemplo de log dos servidores de emails
 
## 4. Remover os serviços
- Comando para parar os serviços:
<br>`$ docker-compose stop`

- Comando para remover os serviços:
<br>`$ docker-compose rm`

## 5. Licença

Este código é open source (código aberto).
