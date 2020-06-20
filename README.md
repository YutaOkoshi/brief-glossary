

```
$ brew install pyenv
$ pyenv install 3.8.3
$ pyenv global 3.8.3
$ pyenv versions
  system
* 3.8.3 (set by /usr/local/var/pyenv/version)
$ python3 -m venv venv

$ pip install -r requirements.txt

```


```
$ docker-compose run web django-admin.py startproject brief-glossary .
python manage.py startapp 
```

```
$ python -m pip install django-mysql
INSTALLED_APPS = (
    ...
    'django_mysql',
)
Django-MySQL comes with some extra checks to ensure your configuration for Django + MySQL is optimal. It’s best to run these now you’ve installed to see if there is anything to fix:

$ ./manage.py check
```


```
$ python manage.py makemigrations
$ python manage.py migrate
```
