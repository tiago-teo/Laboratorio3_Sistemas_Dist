# Laboratorio3_Sistemas_Dist
 Using python and django to create a api with web services. This project has the objective of creating an interface with administrators and simple users. 
 Administrators can add, edit, delete, packages information. Additionaly they can see what users exist and add, edit or delete them.
 Users can list they're packages, search for a specific package and see all the information related to their packages
 Packages have an id, sender, receiver, name, description, sender city, destination city, tracking, status

## Requirements
 - python
 - pip (optional)
 - pip install django or sudo pacman -S python-django (ArchLinux)
 - pip install django-rest-framework or sudo pacman -S python-django-rest-framework (ArchLinux)

## How to Use
### Setup
 - git clone https://github.com/tiago-teo/Laboratorio3_Sistemas_Dist/
 - cd Laboratorio3_Sistemas_Dist/laboratorio3/
 - python manage.py makemigrations
 - python manage.py migrate
 - python manage.py runserver

### Creating superuser
 - Ctrl + C to stop server if its running
 - python manage.py createsuperuser (Fill out information)
 - python manage.py runserver
 - Go to /admin/ and try to login

### List of pages
 - /
 - /admin/
 - /login/
 - /register/
 - /packages
 
