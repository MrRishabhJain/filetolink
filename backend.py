from flask import Flask, render_template, request, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
import random
import os

app = Flask(__name__)
CORS(app)

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
		return r
	else:
		return 'Error!'

	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		os.chdir('.data')
		n=random.randint(1000,9999)
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
