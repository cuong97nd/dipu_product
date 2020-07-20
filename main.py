import excel
import time

from flask import Flask, request, render_template ,send_from_directory
UPLOAD_DIR = './upload/'
DOWNLOAD_DIR = './download/'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        time_start = time.time()
        try :
          f = request.files['file1']
          f.save(UPLOAD_DIR + f.filename)
        
          excel_res=excel.excel( UPLOAD_DIR + f.filename,DOWNLOAD_DIR + f.filename)
        except KeyError as e :
          return render_template(
            'jinja_upload.html', message='エラー！チェックしたいシットワックは必ずSheet11に設定してください' , link = '', res=[])
        except IsADirectoryError as e :
          return render_template(
            'jinja_upload.html', message='ファイルを選択してください' , link = '', res=[])
        except :
          return render_template(
            'jinja_upload.html', message='エラー' , link = '', res=[])
        
      
        time_end = time.time()
        return render_template(
            'jinja_upload.html', message='完了です' , link = 'https://dipu.cuonhbui.repl.co/download/' + f.filename , res=excel_res, time_m =int((time_end - time_start)/60) , time_s =int(time_end - time_start)%60 ) 
    else:
        return render_template('jinja_upload.html', message="" ,link ='' , res=[])

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory('./download/',
                               filename, as_attachment=True)

app.run(host='0.0.0.0', port=8080)