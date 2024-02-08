from flask import Flask, render_template

app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    params = {
        'title': 'Заголовок',
        'surname': 'Фамилия',
        'name': 'Имя',
        'education': 'Образование',
        'profession': 'Профессия',
        'sex': 'Пол',
        'motivation': 'Мотивация',
        'ready': True
    }
    return render_template('answer.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
