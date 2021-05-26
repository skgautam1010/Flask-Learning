from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

import json

with open("config.json","r") as f:
    params=json.load(f)["params"]

localserver=True
app = Flask(__name__)
if localserver:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db=SQLAlchemy(app)


class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String(50),unique=False,nullable=False)
    lname = db.Column( db.String( 50 ), unique=False, nullable=False )
    contact = db.Column( db.String( 12 ), unique=True, nullable=False )
    email = db.Column( db.String( 255 ), unique=True, nullable=False )
    msg = db.Column( db.String( 100 ), unique=False, nullable=False )

@app.route('/index.html')
def index():
    return render_template('index.html',params=params)

@app.route('/aboutus.html')
def aboutus():
    return render_template('aboutus.html',params=params)


@app.route("/contactus.html",methods=['GET','POST'])
def contact():
    if(request.method=='POST'):
        f_name=request.form.get('firstname')
        l_name=request.form.get('lastname')
        contactus=request.form.get('telephone')
        emailid=request.form.get('emailid')
        feedback=request.form.get('feedback')

        entry=Contact(fname=f_name,lname=l_name,contact=contactus,email=emailid,msg=feedback)
        db.session.add(entry)
        db.session.commit()
    return render_template('contactus.html',params=params)

app.run(debug=True)