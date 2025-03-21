


## Setup
Django upgraded to 5.1
Python version 3.12

The first thing to do is to clone the repository:

```sh
git clone https://github.com/mohammedwed/Lushlyrics-insecure.git
cd lushlyrics-webapp-django
```

Create a virtual environment to install dependencies in and activate it:

```sh
virtualenv2 --no-site-packages env
source env/bin/activate
```

With Python venv:
```sh
python -m venv virtual_environment_name
```

In Windows:
```sh
virtual_environment_name\Scripts\activate
```

In macOS and Linux:
```sh
source virtual_environment_name\bin\activate
```

Then install the dependencies:

```sh
pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Once `pip` has finished downloading the dependencies:
```sh
cd Lushlyrics-insecure
python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

To make password reset process work, you have to create a .env file and write your environment variables:
```
EMAIL_HOST_USER='admin_mail'
EMAIL_HOST_PASSWORD='admin_mail_password_generated_for_apps'
```

If you don't know how to generate a password for apps, google has it's own tutorial.
