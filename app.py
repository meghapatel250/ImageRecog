from flask import Flask, render_template, request
import os
from model import predict_image
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('error.html', message="No file part in the request.")
    file = request.files['file']
    if file.filename == '':
        return render_template('error.html', message="No file selected.")
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Get prediction from the model
        label, confidence = predict_image(filepath)
        return render_template('result.html', label=label, confidence=confidence, filepath=filepath)
    
    return render_template('error.html', message="File type not allowed.")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

