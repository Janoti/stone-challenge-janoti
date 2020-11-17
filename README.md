stone-challenge
Para rodar localmente:

-- Instale o Docker: apt install docker

-- Clone o repositorio da app

-- Dentro do diretório, rode:

-- $ docker build ./ -t challenge-stone # para buildar o container

-- Confira se seu container está ok:

-- $ docker images # procure pelo imagem challenge-stone

-- Rode $ docker run -p 5000:5000 challenge-janoti #para executar mapeando a porta 5000

-- Abra seu navegador e digite: http://127.0.0.1:5000/users

Rotas

-- http://127.0.0.1:5000/users #retorna a lista de usuários

-- http://127.0.0.1:5000/users/cpf #retorna o usuário pesquisando pelo cpf

-- Para inserir um novo usuário, substitua os dados do usuário na estrutura abaixo:

Acesso pelo PAAS Heroku:

-- Retorna a lista de usuários

https://stone-challenge-janoti.herokuapp.com/users

-- Retorna o usuário pesquisando pelo cpf

https://stone-challenge-janoti.herokuapp.com/users/

-- Para inserir um novo usuário, substitua os dados do usuário na estrutura abaixo:

curl --location --request POST 'https://stone-challenge-janoti.herokuapp.com/users' \--header 'Content-Type: application/json' \--data-raw '{
 "nome": "InsiraSeuNome",
 "sobrenome": "InsiraSeu Sobrenome",
 "cpf": 122312321321,
 "email": "ninguemusa@yahoo.com.br",
 "data_nasc": "19/01/1989"
