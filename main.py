#pip install flask opencv-python
import os
import cv2
from flask import Flask , render_template, request, flash,redirect, url_for
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'webp', 'png', 'jpg', 'jpeg', 'gif'}

def processImage(filename , operation):
    print(f"The operation is {operation} and the filename is {filename}")
    img = cv2.imread(f"uploads/{filename}")
    match operation:
        case "cgray":
           imgprocessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
           newfilename = f"static/{filename}"
           cv2.imwrite(newfilename, imgprocessed)
           return newfilename
        case "cpng":
           newfilename = f"static/{filename.split('.')[0]}.png"
           cv2.imwrite(newfilename, img)
           return newfilename
        case "cwebp":
           newfilename = f"static/{filename.split('.')[0]}.webp"
           cv2.imwrite(newfilename, img)
           return newfilename
        case "cjpg":
           newfilename = f"static/{filename.split('.')[0]}.jpg"
           cv2.imwrite(newfilename, img)
           return filename
    pass  

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/edit",methods=["GET", "POST"])
def edit():
    if request.method == 'POST':
        operation = request.form.get("operation")
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new = processImage(filename , operation )
            flash(f"Your image has been processed and is avaiable <a href='/{new}' target= '_blank'> here </a>")
            return render_template("index.html")
    
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        name = request.form.get('username')
        post = request.form.get('password')
        # still need to complete

    return render_template("login.html")

app.run(debug=True,port=5001)