import re,random,os
from flask import render_template, request, redirect, flash,make_response,session,url_for
from sqlalchemy.sql import text

from werkzeug.security import generate_password_hash,check_password_hash
from areaapp import app
from areaapp.forms import SignupForm
from areaapp.models import Admin,User,db



@app.route('/admin/layout')
def admin_layout():
    return render_template ('admin/layout.html')