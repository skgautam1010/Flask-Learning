from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus.html')
def aboutus():
    return render_template('aboutus.html')

@app.route("/bootstrap")
def bootstrap():
    return render_template('bootstrap.html')

@app.route("/contactus.html")
def contact():
    return render_template('contactus.html')
app.run(debug=True)