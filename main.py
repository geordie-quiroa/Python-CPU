from flask import Flask
from flask import render_template
from circuitoIntegrado import CI
app = Flask(__name__)



@app.route('/')
def site(test=0):
    return render_template('index.html', test=test)