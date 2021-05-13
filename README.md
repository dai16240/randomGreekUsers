![logo](static/img/favicon.png)
# randomGreekUsers

#### Generate fake random user data in Greek.

randomGreekUsers is an API that generates fake random Greek user data, in JSON format.
Built with Flask/Python.

Check it out [here](https://randomgreekusersapi.herokuapp.com).

## Usage

- GET [/api/user](https://randomgreekusersapi.herokuapp.com/api/user)
Get data for a single user.
- GET [/api/users/10](https://randomgreekusersapi.herokuapp.com/api/users/10)
Get data for _10_ users.

## Installation
randomGreekUsers requires [Python](https://www.python.org/) 3 to run.
- Create a virtual environment.
- Install the dependencies from _requirements.txt_ and run the application using gunicorn.

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
gunicorn main:app
```
