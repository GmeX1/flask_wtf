from flask import Flask, render_template

app = Flask(__name__)


@app.route('/distribution')
def distribution(people=None):
    if people is None:
        people = ['Риддли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('distribution.html', people=people)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
