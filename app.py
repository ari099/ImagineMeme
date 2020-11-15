#!/bin/python

from flask import *
from PIL import Image, ImageDraw, ImageFont
from werkzeug.utils import *

UPLOAD_FOLDER = '.\\img'
FONTS_FOLDER = '.\\fonts'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

# Flask app object...
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['FONTS_FOLDER'] = FONTS_FOLDER

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', page='Home Page')

@app.route('/imagine/', methods=['POST'])
def imagine():
    # Load form data
    img = request.files['img-upload'];
    topText = request.form['top-text']
    bottomText = request.form['bottom-text']

    # Save image
    filename = secure_filename(img.filename)
    img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # Add text to picture
    newImg = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    img_width, img_height = newImg.size
    draw = ImageDraw.Draw(newImg)
    font_size = 90
    font = ImageFont.truetype(os.path.join(app.config['FONTS_FOLDER'], 'IMPACT.TTF'), font_size)
    size_width, size_height = draw.textsize(topText, font)
    while size_width > img_width:
        font_size -= 1
        font = ImageFont.truetype(os.path.join(app.config['FONTS_FOLDER'], 'IMPACT.TTF'), font_size)
        size_width, size_height = draw.textsize(topText, font)
    
    while size_width < img_width:
        font_size += 1
        font = ImageFont.truetype(os.path.join(app.config['FONTS_FOLDER'], 'IMPACT.TTF'), font_size)
        size_width, size_height = draw.textsize(topText, font)
    
    draw.text((0, 0),topText,(255,255,255),font=font)
    
    font = ImageFont.truetype(os.path.join(app.config['FONTS_FOLDER'], 'IMPACT.TTF'), font_size)
    size_width, size_height = draw.textsize(bottomText, font)
    while size_width > img_width:
        font_size -= 1
        font = ImageFont.truetype(os.path.join(app.config['FONTS_FOLDER'], 'IMPACT.TTF'), font_size)
        size_width, size_height = draw.textsize(bottomText, font)
    
    while size_width < img_width:
        font_size += 1
        font = ImageFont.truetype(os.path.join(app.config['FONTS_FOLDER'], 'IMPACT.TTF'), font_size)
        size_width, size_height = draw.textsize(bottomText, font)
    
    draw.text((0, img_height-size_height),bottomText,(255,255,255),font=font)
    newImg = newImg.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    # Send new pic
    safe_path = safe_join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(safe_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
