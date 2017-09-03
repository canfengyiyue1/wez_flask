import os
from app import create_app, db
from app.models import all_models
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


if os.path.exists('.env'):
    print('Import enviroment form .env ...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

app = create_app(os.getenv('FLASK_CONFIG') or 'default')



if __name__ == '__main__':
    app.run()
