from flask import Flask

# WSGI object, used to interact between server and the web application
app = Flask(__name__)

# decorator
@app.route('/')
def hello():
    return "Hello World!"


@app.route('/gourab')
def gourab():
    return "Hello Gourab!"


if __name__ == "__main__":
    app.run(debug=True)