import re,random,os
from flask import render_template, request, redirect, flash,make_response,session,url_for
from sqlalchemy.sql import text

from werkzeug.security import generate_password_hash,check_password_hash
from areaapp import app
from areaapp.forms import SignupForm
from areaapp.models import Admin,User,db



@app.route('/layout')
def layout():
    return render_template('layout.html')
    

@app.route('/signin')
def signin():
    return 'done'

@app.route("/register" ,methods=['POST','GET'])
def register():
    Signupform= SignupForm()
    if request.method=='GET':
        return render_template("user/signup.html",Signupform=Signupform)
    else:
        if Signupform.validate_on_submit():
            userpass=request.form.get('password')
            u=User(user_fullname=request.form.get('fullname'),
                   user_email=request.form.get('email'),
                   user_pwd=generate_password_hash(userpass))
            db.session.add(u)
            db.session.commit()
            session['userid']=u.user_id
            session['user_loggedin']=True
            return redirect('/dashboard')
            # flash('account created successfully')
            # return redirect('/login')
        else:
            return render_template('user/signup.html',Signupform=Signupform)