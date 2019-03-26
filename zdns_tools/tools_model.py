from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField, BooleanField
from wtforms.validators import DataRequired,Email,Length,EqualTo

class RegisterForm(FlaskForm):
    username = StringField(label="用户名", validators=[DataRequired,Length(1,32)])
    password = PasswordField(label="密码",validators=[DataRequired,EqualTo('password2',message="密码必须相同")])
    password2 = PasswordField(label="确认密码",validators=[DataRequired,Length(1,16)])
    submit = SubmitField(label='注册')
