# mobills-clone
# Passos Iniciais neste Projeto

# Criando a máquina virtual
```bash
$ python -m venv ./venv
```

# Comando para ativar a venv no pycharm com cmd
```bash
$ venv\Scripts\activate.bat
```

# Comando para desativar a venv
```bash
$ venv\Scripts\deactivate.bat
```

# Instalando o django
```bash
$ pip install django
```

# Criando o projeto django
```bash
$ django-admin startproject setup .
```

# Instalando a lib de banco de dados postgresql
```bash
$ pip install psycopg2
```


# Criando o app 'despesa'
```bash
$ python manage.py startapp despesa
```

# Atualizando as requirements
```bash
$ pip install -r requirements.txt
```

# Depois rodar o comando abaixo para coletar os arquivos estaticos
```bash
$ python manage.py collectstatic
```

# Toda vez que mexer no model, precisa reexecutar as Migrations
```bash
$ python manage.py makemigrations
```

# Aplica as migrations no banco de dados
```bash
$ python manage.py migrate
```

# Criando o super usuario
```bash
$ python manage.py createsuperuser
```
# Dados Usuario
    * Usuario:admin
    * Senha:123456

# Rodando o projeto
```bash
$ python manage.py runserver
```

###############################################################
# Criando o app 'receita'
```bash
$ python manage.py startapp receita
```
