from flask import Flask, render_template

app = Flask('Projeto Panther')

@app.route("/")
def home():
    return render_template('home.html'), 200

@app.route('/about')
def about():
    return render_template('about.html'), 200

@app.route('/historia')
def historia():
    return "historia da pant", 200

app.config['DEBUG'] = True
app.run(host='0.0.0.0', port=80)
