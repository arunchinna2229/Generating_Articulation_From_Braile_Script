import cv2
import tempfile
import os
import uuid
from flask import Flask,jsonify,render_template,send_file,redirect,request
import alphaToBraille,brailleToAlpha,printer
# from werkzeug import secure_filename
from werkzeug.utils import secure_filename
from OBR import SegmentationEngine,BrailleClassifier,BrailleImage
from audio import text_to_speech


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
# tempdir = tempfile.TemporaryDirectory()

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__) #creating the Flask class object  
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

 
@app.route('/') #decorator drfines the   
def home():  
    return render_template('index.html')



@app.route("/text-to-braille",methods=['GET','POST'])
def text_to_braille():
    if request.method == "POST":
        txt = request.form['voiced']
        res = alphaToBraille.translate(txt)
        return render_template('res_t2b.html',result=res,text=txt)



@app.route("/braille-to-text",methods=['GET','POST'])
def braille_to_text():
    if request.method == "POST":
        txt = request.form['text']
        res = brailleToAlpha.translate(txt)
        try:
            text_to_speech(res)
        finally:
            return render_template('res_b2t.html',result=res,braille_text=txt)




@app.route('/digest', methods=['GET','POST'])
def upload():
    if request.method=='POST':
        f=request.files['file']
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            image_path = '{}/{}'.format(UPLOAD_FOLDER,filename)
            classifier = BrailleClassifier()
            img = BrailleImage(image_path)
            for letter in SegmentationEngine(image=img):
                letter.mark()
                classifier.push(letter)
            cv2.imwrite('{}/{}-proc.png'.format(UPLOAD_FOLDER,filename), img.get_final_image())
            res = str(classifier.digest())
            res = res.replace('*','')
            x = filename+'-proc.png'
            text_to_speech(res)
            return render_template('res_img.html',text=res,filename=x)



@app.route('/img2braille', methods=['GET','POST'])
def upload_img():
    import pytesseract
    from PIL import Image
    if request.method=='POST':
        f=request.files['file']
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            
            image_path = '{}/{}'.format(UPLOAD_FOLDER,filename)
            img = Image.open(image_path)
            pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'   
            result = pytesseract.image_to_string(img)

            res = alphaToBraille.translate(result)
            return render_template('res_t2b.html',result=res,text=result)

  
if __name__ =='__main__':  
    app.run(debug = True)
    UPLOAD_FOLDER.cleanup()
