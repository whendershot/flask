from flask import Flask, render_template, request, redirect, session
import os
from db import db

app = Flask(__name__.split('.')[0])
app.secret_key = os.environ.get('KEY')

@app.route('/')
def index_load():
    if not 'surveys' in session:
        session['surveys'] = []

    return render_template('./user_survey.html', data=db)

@app.route('/process', methods=['POST'])
def process_form():
    print(request.form)
    session['latest_survey'] = {
        'name' : request.form['user_name'],
        'location' : request.form['dojo_location'],
        'languages' : request.form.getlist('languages'),
        'comment' : request.form['comment']
    }
    session['surveys'].append(session['latest_survey'])
    return redirect('/result')

@app.route('/result')
def show_result():
    return render_template('./user_form_display.html', survey=session['latest_survey'])

@app.route('/surveys')
def show_surveys():
    return render_template('./surveys.html', surveys=session['surveys'])

@app.route('/', defaults={'u_path' : ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
    print(repr(u_path))
    return f'Sorry! No response. Try again. But how did you fall into here?<br>{u_path}'


if __name__ == '__main__':
    app.run(debug=True)