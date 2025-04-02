from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db
from routes import init_routes

app = Flask(__name__)

CORS(app)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_signup.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app) 

with app.app_context():
    db.create_all()

init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
