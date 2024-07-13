from flask import Flask, request, render_template, redirect, url_for, send_file, make_response
from werkzeug.utils import secure_filename
from models import models
import shutil
import os

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')
SAVE_FOLDER = os.path.join(os.getcwd(), 'save')
MODELS_FOLDER = os.path.join(os.getcwd(), 'models')

app = Flask(__name__, template_folder='./templates/', static_folder='./static/')


@app.route('/NEAT-Config-Editor/')
def index():
    fileDefault = models.File(path=os.path.join(MODELS_FOLDER, 'configDefault.txt'))
    for p, i in enumerate(fileDefault.listLines):
        if i == 'True':
           fileDefault.listLines[p] = 'checked'
        elif i == 'False':
            fileDefault.listLines[p] = ''

    return render_template('index.html', parameters=fileDefault.listLines)


@app.route('/NEAT-Config-Editor/upload/', methods=['POST'])
def upload():
    countFiles = models.count_files(UPLOAD_FOLDER)
    savePath = os.path.join(UPLOAD_FOLDER, secure_filename(f'config{countFiles}.txt'))
    request.files['file'].save(savePath)

    return redirect(url_for('indexUpload', id=countFiles))


@app.route('/NEAT-Config-Editor/<int:id>')
def indexUpload(id):
    try:
        file = models.File(path=os.path.join(UPLOAD_FOLDER, f'config{id}.txt'))
        for p, i in enumerate(file.listLines):
            if i == 'True':
               file.listLines[p] = 'checked'
            elif i == 'False':
                file.listLines[p] = ''
            if file.parameters[p] in file.percentages:
                file.listLines[p] = int(float(file.listLines[p]) * 100)

        return render_template('index.html', parameters=file.listLines)
    except Exception:
        return

@app.route('/NEAT-Config-Editor/save/', methods=['POST'])
def save():
    arq = models.File(parameters=request.form.to_dict())
    arq.save('./save/config.txt')
    file = os.path.join(SAVE_FOLDER, 'config.txt')
    response = make_response(send_file(file, mimetype='text/plain'))
    response.headers['Content-Disposition'] = 'attachment; filename=config.txt'
    return response


@app.route('/NEAT-Config-Editor/delete/', methods=['GET'])
def delete():
    for item in os.listdir(UPLOAD_FOLDER):
        item_path = os.path.join(UPLOAD_FOLDER, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        elif os.path.isfile(item_path):
            os.remove(item_path)
    try:
        if os.path.exists(os.path.join(MODELS_FOLDER, '__pycache__')):
            shutil.rmtree(os.path.join(MODELS_FOLDER, '__pycache__'))
    except:
        pass
    return redirect(url_for('index'))


@app.route('/NEAT-Config-Editor/error/<int:errorID>')
def error(errorID):
    if errorID in [1]:
        return render_template('error.html', error=errorID)
    else:
        return redirect(url_for('index'))


@app.route('/NEAT-Config-Editor/download/')
def download():
    file = './models/configDefault.txt'
    response = make_response(send_file(file, mimetype='text/plain'))
    response.headers['Content-Disposition'] = 'attachment; filename=config.txt'
    return response


if __name__ == '__main__':
    app.run()
