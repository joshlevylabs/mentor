# mentor
https://virtualenv.pypa.io/en/latest/user_guide.html#introduction}
https://www.markdownguide.org/basic-syntax/


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
