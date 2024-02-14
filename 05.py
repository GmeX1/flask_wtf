from flask import Flask, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    id_astronaut = StringField('ID Астронавта', validators=[DataRequired()])
    pwd_astronaut = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_captain = StringField('ID Капитана', validators=[DataRequired()])
    pwd_captain = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Получить доступ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
