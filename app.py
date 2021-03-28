from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/sonu')
def hello_sonu():
    return 'Hello, Sonu Bhai!'

app.run(debug=True)