from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


class Admin(db.Model):
    id_admin=db.Column(db.Integer, autoincrement=True,primary_key=True)
    admin_username=db.Column(db.String(20),nullable=True)
    admin_password=db.Column(db.String(200),nullable=True)

class User(db.Model):
    user_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    first_name=db.Column(db.String(20),nullable=True)
    last_name=db.Column(db.String(20),nullable=True)
    email=db.Column(db.String(20),nullable=True)
    password=db.Column(db.String(20),nullable=True)
    phone_number=db.Column(db.String(20),nullable=True)
    date_of_birth=db.Column(db.DateTime(), default=datetime.utcnow)
    

class Category(db.Model):
    category_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    cat_name=db.Column(db.String(20),nullable=False)


    #set relationship
    bookdeets=db.relationship('Book',back_populates='catdeets')

class Image(db.Model):
    id_image=db.Column(db.Integer, autoincrement=True,primary_key=True)
    image_name=db.Column(db.String(20),nullable=True)
    productid=db.Column(db.Integer, db.ForeignKey('product.id_product'),nullable=False) 

class Plan(db.Model):
    plan_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    plan_name=db.Column(db.String(50),nullable=True)
    plan_amount=db.Column(db.Float(200),nullable=True)

class Product(db.Model):
    id_product=db.Column(db.Integer, autoincrement=True,primary_key=True)
    product_name=db.Column(db.String(50),nullable=True)
    product_price=db.Column(db.Float(200),nullable=True)
    product_by_user=db.Column(db.Integer, db.ForeignKey('user.userid'),nullable=False) 
    product_upload_date=db.Column(db.DateTime(), default=datetime.utcnow)


class State(db.Model):
    id_state=db.Column(db.Integer, autoincrement=True,primary_key=True)
    state_name=db.Column(db.String(50),nullable=True)
    city=db.Column(db.String(50),nullable=True)
    user_state=db.Column(db.Integer, db.ForeignKey('user.user_id'),nullable=False) 


class Subscription(db.Model):
    sub_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    start_date=db.Column(db.DateTime(), default=datetime.utcnow)
    end_date=db.Column(db.DateTime(), default=datetime.utcnow)
    plan_id=db.Column(db.Integer, db.ForeignKey('plan.plan_id'),nullable=False) 
    user_id=db.Column(db.Integer, db.ForeignKey('user.userid'),nullable=False) 