# Creating url dyanmically
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

    

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score > 50:
        res = "PASS"
    else:
        res = "FAIL"
    exp = {'score': score, 'res': res}
    return render_template('results.html', result= exp)



@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        math = float(request.form['math'])
        data_science = float(request.form['data-science'])
        c = float(request.form['c'])
    total_score = (math + c + data_science) / 3
    return redirect(url_for('success', score= total_score))



if __name__ == '__main__':
    app.run(debug=True)