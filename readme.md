para iniciar um projeto django usar o comando

```django-admin startproject <NOME_DO_PROJETO>```


Para iniciar/start da aplicação utilizar o comando dentro da pasta do projeto

```python manage.py runserver```


Para inicialiazar o banco de dados default com as configs iniciais usar o comando

```python manager.py migrate```


Toda vez que realizar uma criação de um model ou alterar um model existente tem que executar o comando abaixo para realizar a atualizção/criação do mesmo

```python manager.py makemigrations```

depois de executar o makemigrations é só executar novamente o migrate para efetivar a atualizção/criação.


Apos executar o comando de config default da base de dados podemos criar usuarios para logar na aplicacao/area de administracao django com o comando

```python manage.py createsuperuser```


Para criar ou adicionar os modulos, na raiz do projeto utilizar o comando comando abaixo

```python manage.py startapp NOME_DO_MODULO```


Toda vez que criar um modulo novo precisa realizar o registro em 2 componentes

```app/settings.py```

adicionar a configuracao do apps.py do modulo novo no array INSTALLED_APPS

```app/urls.py```

adicionar a rota de contexto do modulo novo, tambem deve ser criado o arquivo de urls.py no modulo novo para fazer o gerenciamento das rotas do modulo, após adicionar o arquivo tbm deve criar os metodos das requisições nas views.py 
