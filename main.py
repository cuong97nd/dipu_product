

from flask import Flask, request, render_template ,send_from_directory
UPLOAD_DIR = './upload/'

app = Flask(__name__, static_folder='./upload/')



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file1']
        f.save(UPLOAD_DIR + f.filename)
        return render_template(
            'jinja_upload.html', message='Uploaded ' + UPLOAD_DIR + f.filename)
    else:
        return render_template('jinja_upload.html', message="")

@app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['upload'],
                               filename, as_attachment=True)

app.run(host='0.0.0.0', port=8080)