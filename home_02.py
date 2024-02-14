from flask import Flask, render_template

app = Flask(__name__)


@app.route('/table/<sex>/<age>')
def table(sex='male', age=25):
    if type(age) is str:
        age = int(age)
    return render_template('table.html', sex=sex, age=age)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
