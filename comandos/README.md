# Agenda

Iniciar um projeto Django

'''
python -m venv venv
. venv/scripts/activate
pip install Django
Django-admin startproject project .
python manage.py startapp contact
'''

Configurar o Git

'''
git config --global user.name
git config --global user.email
git config --global init.defaultbranch main
git init
git add .
git commit
git remote add origin url
'''

Migrando a base de dados do Django

'''
python manage.py makemigrations
python manage.py migrate
'''

Criando e modificando a senha de um super usuário Django
'''
python manage.py createsuperuser
python manage.py changepassword USERNAME
'''