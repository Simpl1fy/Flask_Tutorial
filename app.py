# Creating url dyanmically
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"

@app.route('/pass/<int:score>')
def success(score):
    return "Person has passed with score :" + score

@app.route('/fail/<int:score>')
def fail(score):
    return "Person has failed with score: " + score

if __name__ == '__main__':
    app.run()