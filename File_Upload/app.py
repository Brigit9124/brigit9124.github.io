from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    filename = file.filename

    save_path = os.path.join(UPLOAD_FOLDER, filename)

    file.save(save_path)

    return render_template('success.html', filename=filename)


@app.route('/files/<path:filename>')
def files(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route('/read')
def read_file():
    name = request.args.get('name')

    path = os.path.join(UPLOAD_FOLDER, name)

    try:
        with open(path, 'r') as f:
            return f.read()
    except:
        return 'error'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)