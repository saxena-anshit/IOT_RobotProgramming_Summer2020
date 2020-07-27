from flask import *
from Image_recognition import detect
import os

PEOPLE_FOLDER = os.path.join('static', 'images')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
def upload():
    return render_template("file_upload_form.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        det= detect(f)
        # img.save(f.filename + "New")
        # f.save(f.filename)
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], "New_" + f.filename)
        return render_template("success.html", name=f.filename, image=full_filename, detection= det)





if __name__ == '__main__':
    app.run(debug=True)