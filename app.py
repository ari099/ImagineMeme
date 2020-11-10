#!/bin/python

from flask import *

# Flask app object...
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', page='Home Page')

@app.route('/about/', methods=['GET'])
def about():
    return render_template('about.html', page='Home Page')

@app.route('/contact/', methods=['GET'])
def contact():
    return render_template('contact.html', page='Home Page')

@app.route('/imagine/', methods=['POST'])
def imagine():
    return jsonify({'test': 'Did this work?'})

if __name__ == '__main__':
    app.run(debug=True)
