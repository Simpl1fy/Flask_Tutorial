# Creating url dyanmically
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"

@app.route('/pass/<int:score>')
def success(score):
    return "Person has passed with score :" + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "Person has failed with score: " + str(score)

@app.route('/result/<int:marks>')
def results(marks):
    result=""
    if marks > 50:
        result = "success"
    else:
        result = "fail"
    return redirect(url_for(result, score= marks))


if __name__ == '__main__':
    app.run(debug=True)