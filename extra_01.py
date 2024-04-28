import glob
import os

from flask import Flask, render_template, request

app = Flask(__name__)


def update_images():
    global images
    images = glob.glob('static\\img\\*.*g')


@app.route('/', methods=['GET', 'POST'])
@app.route('/galery', methods=['GET', 'POST'])
def gallery():
    global images
    if request.method == 'POST' and 'file' in request.files:
        f = request.files['file']
        f.save(os.path.join('static', 'img', f.filename))
        update_images()
    return render_template('gallery.html', images=images)


if __name__ == '__main__':
    images = list()
    update_images()
    app.run(port=8080, host='127.0.0.1')
