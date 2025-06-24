from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Email,Length
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
bootstrap = Bootstrap5(app)
class MyForm(FlaskForm):
    valid_mail = Email(message="not a valid email")
    email = StringField(label='Email',validators=[DataRequired(),valid_mail])
    password = PasswordField(label='Password',validators=[DataRequired(),Length(min=8)])
    submit = SubmitField(label="Log In")
app.secret_key = "Ashmiku"
@app.route("/")
def home():
    return render_template('index.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)
