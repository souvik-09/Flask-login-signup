from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:12345@localhost:8888/user_signup'


db=SQLAlchemy(app)
 
class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer,primary_key=True)
    username_=db.Column(db.String(120))
    email_=db.Column(db.String(120),unique=True)
    password_=db.Column(db.String(120))
    cpassword=db.Column(db.String(120))
 
    def __init__(self,username_,email_,password_,cpassword_):
        self.username_=username_
        self.email_=email_
        self.password_=password_
        self.cpassword=cpassword_

@app.route("/")
def signup():
    return render_template("signup.html")

@app.route("/success", methods =['POST'])
def success():
    if request.method == 'POST':
        username = request.form["username_name"]
        email = request.form["email_name"]
        password = request.form["password_name"] 
        cpassword = request.form["cpassword_name"]
        print(username, email, password, cpassword)
        data=Data(username,email,password,cpassword) 
        db.session.add(data)
        db.session.commit()
        return render_template("success.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/table")
def table():
    return render_template('table.html')    
    

if __name__=='__main__':
    app.debug = True
    app.run()     

    