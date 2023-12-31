from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'haha'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path.abspath("website/" + DB_NAME)}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    return app

def create_database(app):
    db_path = path.abspath("website/" + DB_NAME)
    print("Database Path:", db_path)

    if not path.exists(db_path):
        with app.app_context():
            db.create_all()
            print('Created database!')
    else:
        print('Database file already exists.')

if __name__ == '__main__':
    app = create_app()
    create_database(app)
    app.run(debug=True)


    



