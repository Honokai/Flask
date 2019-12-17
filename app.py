from flask import Flask, render_template, url_for

app = Flask('Projeto Panther')

post = [
    { 
        'author': 'Emerson',
        'title': 'Some shit',
        'date_posted': '12/23/2019',
        'description': 'As i said some other time, it didnt work at all'
    },
    {
        'author': 'yuri',
        'title': 'Somese',
        'date_posted': '12/23/2019',
        'description': ' Hollow '
    }

]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Sorting', post=post)

@app.route("/login")
def log():
    return render_template('login.html'), 200

@app.route('/about')
def about():
    return render_template('about.html', title='About'), 200

@app.route('/historia')
def historia():
    return "historia da pant", 200

app.config['DEBUG'] = True
app.run(host='0.0.0.0', port=80)