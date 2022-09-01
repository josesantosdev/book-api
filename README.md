# Book Api

## Dependencies

- Flask
- flask_sqlalchemy
- flask_migrate
- flask_marshmallow
- marshmallow_sqlalchemy

## How to run this project.

```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

pip install requirements.txt

flask run
```

## How to make the migrations

```sh
flask db init
flask db migrate
flask db upgrade
```