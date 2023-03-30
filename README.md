# IGS Employee Manager

Esta aplicação tem como objetivo gerenciar a informação dos colaboradores, como o nome, endereço de e-mail, e departamento. Consiste em uma API feita com Django como framework e Postgres como banco de dados.

## Como rodar a aplicação?

### 1) Clonar o repositório ou fazer download zip.

### 2) Entrar no diretório gerado após cloná-lo.

## Caso não haja python na máquina, mas haja docker compose:

### 3) Construir o container

```shell
docker-compose build
```

### 4) Rodar o container

```shell
docker-compose up
```

O acesso será em: `http://localhost:8000/`

#### Parar o container quando for necessário

```shell
docker-compose down
```

## Caso haja python na máquina:

### 3) Criar um ambiente virtual.

```shell
python -m venv venv
```

Ou, como no meu caso, utilize a versão do python no final do nome:

```shell
python3 -m venv venv
```

### 4) Ativar o ambiente virtual criado pelo python.

Ele será visível como `venv` e para ativá-lo basta um comando como:

```shell
source venv/bin/activate
```

### 5) Instalar os requisitos para a aplicação rodar:

Primeiro, esteja no mesmo diretório que o requirements.txt, ou seja, mude para o IGS_Employee_Manager

```shell
cd IGS_Employee_Manager
```


```shell
pip install -r requirements.txt
```

O acesso será em: `http://localhost:8000/`

## Acesso ao banco de dados

As migrações foram feitas com:

```shell
python manage.py makemigrations
```

### 1) Migre

Caso estiver em ambiente virtual:

```shell
python manage.py migrate
```

Caso estiver em docker:

```shell
docker-compose run backend python manage.py migrate
```

### 2) Entre com o superuser para checar o painel de administração

Acesse o link em `http://localhost:8000/admin/` e acesse com o superuser para registrar ou remover novos usuários.

```shell
bernardo
pythonandonaigs
```

### Ou faça o seu próprio, se preferir:

Caso estiver em ambiente virtual:

```shell
python manage.py createsuperuser
```

Em docker:

```shell
docker-compose run backend python manage.py createsuperuser
```

## Documentação pelo Swagger:

Você acessá-la em: `http://localhost:8000/swagger/`. Nela, você poderá ver as rotas GET sem autorização, mas para POST ou DELETE será necessário o login com superuser. Podendo ser o que eu criei:

```shell
username: bernardo
password: pythonandonaigs
```
Ou que você criou.

## Documentação pelo Redoc:

Você pode acessá-la em: `http://localhost:8000/redoc/` e as regras são as mesmas que com o Swagger.

## Como visualizar a aplicação?

### No navegador

Você pode ir até o link para uma página HTML `http://localhost:8000/employee_list/`, que não exigirá nenhuma autenticação e você poderá ver a lista de colaboradores e as suas seções.

Pela aplicação ter sido feita utilizando Django Rest Framework, você também tem um bom acesso visual a API no navegador:

Acesso a todos os funcionários:
`http://localhost:8000/api/employees/`

Acesso a todos os departamentos:
`http://localhost:8000/api/departments/`


### No terminal

Você pode acessar essa mesma lista utilizando o comando: 

```shell
curl -H "Content-Type: application/javascript" http://localhost:8000/api/employees/
```

```shell
[
  {
    "name": "Jose da Silva",
    "email": "jose.silva@igs-software.com.br",
    "department": "Tester"
  },
  {
    "name": "Jose dos Santos",
    "email": "jose.santos@igs-software.com.br",
    "department": "Developer"
  },
  {
    "name": "Jose Lima",
    "email": "jose.lima@igs-software.com.br",
    "department": "RH"
  }
]
```

Ou pode visualizar os departamentos e seus colaboradores com:

```shell
curl -H "Content-Type: application/javascript" http://localhost:8000/api/departments/
```

```shell
{
    "departments": [
        {
            "id": 1,
            "name": "Tester",
            "employees": [
                {
                    "id": 1,
                    "department": 1,
                    "name": "Jose da Silva",
                    "email": "jose.silva@igs-software.com.br"
                }
            ]
        },
        {
            "id": 2,
            "name": "Developer",
            "employees": [
                {
                    "id": 2,
                    "department": 2,
                    "name": "Jose dos Santos",
                    "email": "jose.santos@igs-software.com.br"
                }
            ]
        },
        {
            "id": 3,
            "name": "RH",
            "employees": [
                {
                    "id": 3,
                    "department": 3,
                    "name": "Jose Lima",
                    "email": "jose.lima@igs-software.com.br"
                }
            ]
        }
    ]
}

```

## Como adicionar ou remover colaboradores pelo terminal ou plataforma de API?

Estes métodos podem ser feitos facilmente pela documentação Swagger ou o próprio Django Admin, em ambos será necessário ser um superuser, com isso, você poderá adquirir o seu token de autenticação. Porém, se for de desejo testar as rotas no próprio terminal, as regras são as mesmas e os comando serão explicitados abaixo, onde utilizei o meu superuser criado anteriormente: 

```shell
curl -X POST -d "username=bernardo&password=pythonandonaigs" http://localhost:8000/api/token-auth/
```

O que tenho como retorno é um token que precisarei utilizar na header das requisições:

```shell
{"token":"3e13c1575911981cd091db7134bf56bef4391ded"}
```

Antes de adicionar um colaborador, é necessário que o departamento já exista para utilizarmos o seu ID. Por isso, criarei um novo departamento:

```shell
curl -X POST -H "Content-Type: application/json" -H "Authorization: Token 3e13c1575911981cd091db7134bf56bef4391ded" -d '{"name": "Marketing"}' http://localhost:8000/api/departments/
```

Como retorno, eu tive: 

```shell
{
  "id":4,
  "name":"Marketing"
  }
```

Com o ID obtido, posso adicionar um funcionário no departamento de marketing:

```shell
curl -X POST -H "Content-Type: application/json" -H "Authorization: Token 3e13c1575911981cd091db7134bf56bef4391ded" -d '{"name": "José Arantes", "email": "jose.arantes@igs-software.com.br", "department": 4}' http://localhost:8000/api/employees/
```

E se tudo estiver correto, esta será a minha resposta:

```shell
{
  "id":4,
  "department":4,
  "name":"José Arantes",
  "email":"jose.arantes@igs-software.com.br"
}
```

Para a remoção de um departamento:

```shell
curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Token 3e13c1575911981cd091db7134bf56bef4391ded" http://localhost:8000/api/departments/<department_id>/
```

Por exemplo, o de Marketing:

```shell
curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Token 3e13c1575911981cd091db7134bf56bef4391ded" http://localhost:8000/api/departments/4/
```

Vale-se lembrar que todos os usuários presentes serão removidos também. Logo, para remover apenas um funcionário:

```shell
curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Token 3e13c1575911981cd091db7134bf56bef4391ded" http://localhost:8000/api/employees/<employee_id>/
```

Neste caso, removerei o José Arantes do departamento de Marketing em vez de remover o departamento:

```shell
curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Token 3e13c1575911981cd091db7134bf56bef4391ded" http://localhost:8000/api/employees/4/
```

## Como executar os testes?

### Em docker

```shell
docker-compose run backend python manage.py test employee_manager
```

### Em ambiente virtual

Para executar os testes, certifique-se que com o seu ambiente virtual ainda ativado e, no terminal, digite:

```shell
python IGS_Employee_Manager/manage.py test employee_manager
```

Caso ainda esteja dentro do diretório IGS_Employee_Manager, apenas rode:

```shell
python manage.py test employee_manager
```

## Considerações finais

A princípio, eu utilizaria Postgres por ser o banco de dados que uso de costume, como em produção. Porém, por ser um teste e aplicação que não escalará, optei pelo padrão do Django, o SQLite. Isso permite que eu deixe alguns dados no banco para facilitar a visualização dos mesmos em determinadas páginas. 

Utilizei o Django Rest Framework para uma criação mais assertiva de APIs, além da visualização ser mais clara no painel que nos é disponilizado e utilizei um formatador, black, para deixar o código padronizado. Os vejo como boas práticas ao desenvolver em Python, conhecido por ser assertivo.

Quem rodar o código, provavelmente, tem python instalado na máquina, mas por via das dúvidas, qualquer erro como "na minha máquina não funciona" ou por estar em outra máquina no momento, adicionei o Docker, também pelo costume de utilizar com colegas de equipe.