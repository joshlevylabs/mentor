# mentor
https://virtualenv.pypa.io/en/latest/user_guide.html#introduction}
https://www.markdownguide.org/basic-syntax/
https://devcenter.heroku.com/articles/django-app-configuration
https://devcenter.heroku.com/categories/command-line
https://roadmap.sh/


Start Repo
Clone repo to machine
Run virtualenv
python -m pip install --user virtualenv
virtualenv venv
source venv/bin/activate
Install extensions
python -m pip install Django

Django-admin startproject <newprojectname>
python -m pip freeze > requirements.txt

On 2nd machine, install all requirements from “requirements.txt” file:
    pip install -r requirements.txt


Deploy to Heroku


3 different dev sandboxes
1. local
2. stage environment where it will be a mirror of the production env
3. production


Homework:
1 - Deploy first application
2 - Note application or book catalogue
3 - Incorporate database
4 - Incorporate authentication

ORM - Object relational mapping layer: https://www.fullstackpython.com/django-orm.html
- Layer over my database, abstraction to keep database agnostic from system to system

Learn how to customize
1 - view for listing all notes
2 - view for creating notes
3 - view to update notes
4 - view to delete and confirming delete notes
5 - create folders
6 - put notes into different folders

Blog: https://docs.djangoproject.com/en/3.1/ref/contrib/admin/
Blog: https://simpleisbetterthancomplex.com/archive/
