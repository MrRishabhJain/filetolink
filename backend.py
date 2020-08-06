from flask import Flask, render_template, request, send_file, make_response, Response
from flask_cors import CORS
from werkzeug.utils import secure_filename
import random
import os

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():  # pragma: no cover
    content = open('public/home.html').read()
    return Response(content, mimetype="text/html")

@app.route('/home.css', methods=['GET'])
def css():  # pragma: no cover
    content = open('public/home.css').read()
    return Response(content, mimetype="text/css")

@app.route('/favicon.ico')
def favicon():  # pragma: no cover
	return send_from_directory('public/','favicon.ico', mimetype='image/vnd.microsoft.icon')
    # content = open('public/favicon.ico').read()
    # return Response(content, mimetype="image/vnd.microsoft.icon")

@app.route('/upload')
def upload_file1():
	return render_template('home.html')

@app.route('/download')
def download_file():
	os.chdir('.data')
	key = request.args.get("key")
	if os.path.isdir(str(key)):
		os.chdir(str(key))
		print('list',os.listdir())
		resp = send_file('.data/'+str(key)+'/'+os.listdir()[0], as_attachment=True)
		os.chdir('../../')
		r = make_response( resp )
		r.mimetype = 'application/octet-stream'
		r.headers["Access-Control-Expose-Headers"]="Content-Disposition"
		return r
	else:
		os.chdir('../')
		return 'Error!'


@app.route('/lookup')
def lookup_file():
	os.chdir('.data')
	key = request.args.get("key")
	if os.path.isdir(str(key)):
		os.chdir(str(key))
		_tmp=os.listdir()[0]
		os.chdir('../../')
		return _tmp
	else:
		os.chdir('../')
		return 'Error!'

	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		os.chdir('.data')
		n=random.randint((9999999999999999999999999+1)/10,9999999999999999999999999)
		while os.path.isdir(str(n)):
			n=random.randint(1000,9999)
		os.mkdir(str(n))
		os.chdir(str(n))
		f = request.files['file']
		f.save(secure_filename(f.filename))
		os.chdir('../../')
		return str(n)
		
if __name__ == '__main__':
	app.run(debug = True)
