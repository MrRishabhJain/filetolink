from flask import Flask, render_template, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import random

app = Flask(__name__)
CORS(app)

@app.route('/upload')
def upload_file1():
    return render_template('home.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)
