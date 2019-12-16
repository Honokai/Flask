from flask import Flask, render_template

app = Flask('Projeto Panther')

posts = [
    { 
        'author': 'Emerson',
        'title': 'Some shit',
        'description': 'As i said some other time, it didnt work at all'
    },
    {
        'author': 'yuri',
        'title': 'Somese',
        'description': ' Hollow '
    }

]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route("/login")
def log():
    return render_template('login.html'), 200

@app.route('/about')
def about():
    return render_template('about.html'), 200

@app.route('/historia')
def historia():
    return "historia da pant", 200

app.config['DEBUG'] = True
app.run(host='0.0.0.0', port=80)
