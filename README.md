


## Setup
Django upgraded to 5.1
Python version 3.12

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/mohammedwed/Lushlyrics-insecure.git
$ cd lushlyrics-webapp-django
```

Create a virtual environment to install dependencies in and activate it:
You can use python-dotenv

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd Lushlyrics-insecure
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
