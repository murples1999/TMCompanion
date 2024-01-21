from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/megacredit-calculator")
def megacreditcalculator():
    return render_template('megacredit-calculator.html')

@app.route("/resource-tracker")
def resourcetracker():
    return render_template('resource-tracker.html')

@app.route("/player-reference")
def playerreference():
    return render_template('player-reference.html')

@app.route("/rule-book")
def rulebook():
    return render_template('rule-book.html')

@app.route("/scoring")
def scoring():
    return render_template('scoring.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')