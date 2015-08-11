import os
from flask import render_template, request, Flask, redirect, url_for
from app import app
from werkzeug import secure_filename
from a_Model import ModelIt
from numpy import genfromtxt

# This is new
UPLOAD_FOLDER = './app/upload/'
ALLOWED_EXTENSIONS = set(['csv'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# primary route
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
    	    miRNA_input = genfromtxt(open(os.path.join(app.config['UPLOAD_FOLDER'], filename),'r'), delimiter=',', dtype='f8')[0:,1]
   	    predicted_prob = ModelIt(miRNA_input)
        
            the_result = 1
            test_text = "low"
            if predicted_prob > 0.2:
                the_result = 2
                test_text = "somewhat low"
            if predicted_prob > 0.4:
                the_result = 3
                test_text = "moderate"
            if predicted_prob > 0.6:
                the_result = 4
                test_text = "somewhat high"
            if predicted_prob > 0.8:
                the_result = 5
                test_text = "high" 

        #the_result = ModelIt(miRNA_input)
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	    return render_template("output.html", the_result = the_result, explanation = test_text)
    return render_template("index.html")


@app.route('/basic')
def basic():
    return render_template("basic.html",
        title = 'Home', user = { 'nickname': 'Kyle' },
        )
