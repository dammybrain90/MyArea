from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField,PasswordField
from wtforms.validators import DataRequired,Email,Length,EqualTo
from flask_wtf.file import _FileField,FileAllowed,FileRequired


class contactForm(FlaskForm):
    fullname=StringField('fullname',validators=[DataRequired(message='hello,you should supply all your name')])
    confirm_name=StringField('confirm name',validators=[DataRequired(),EqualTo('fullname',message='do you mean this is same as the previous?')])
    email=StringField('your email',validators=[Email()])
    message=TextAreaField('message',validators=[Length(1,100)])
    btn=SubmitField('send message')




class SignupForm(FlaskForm):
    fullname = StringField("Fullname",validators=[DataRequired(message="your full name is required")])
    email = StringField("Your Email",validators=[Email()])
    password=PasswordField('password',validators=[DataRequired()])
    confirm_password=PasswordField('confirm password',validators=[EqualTo('password',message='confirm password must be equal to password')])
    phone_number=StringField("phone_number",validators=[DataRequired(message="your Phone number is required")])
    Address=StringField("address",validators=[DataRequired()])
    btn = SubmitField("Sign up!")


class profileForm(FlaskForm):
    fullname = StringField("Fullname",validators=[DataRequired(message="your full name is required")])
    pix=_FileField('Display Picture',validators=[FileRequired(),FileAllowed(['jpg','png'],'image only')])
    btn = SubmitField("update profile")
  
    