from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app=Flask(__name__)
app.config['SECRET_KEY']='bca8d343a1705eee510a332ec0f53165b0214651f9e06418'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c21113772:Spring1234@csmysql.cs.cf.ac.uk:3306/c21113772_flaskdatabase1'




db=SQLAlchemy(app)

login_manager = LoginManager(app)



from blog import routes



