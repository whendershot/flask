from flask import Flask, render_template, request, redirect, session
from dataclasses import asdict
import os
from game import controllers

app = Flask(__name__.split('.')[0])
app.secret_key = os.environ.get('KEY')

game_master = controllers.VisitController()

@app.route('/')
def game_loop():
    if not 'is_playing' in session or not session['is_playing']:
        setup()
    
    #advance to the next frame
    return render_template('game.html')

@app.route('/process_money', methods=['POST'])
def process_transaction():
    print(request.form)
    command = request.form.get('command')
    game_master.execute(command, session)
    return redirect('/')

def setup():
    session.clear()
    session['commands'] = game_master.get_commands()
    session['gold_held'] = 0
    session['transaction_hist'] = []
    session['is_playing'] = True


@app.route('/', defaults={'u_path' : ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
    print(repr(u_path))
    return f'Sorry! No response. Try again. But how did you fall into here?<br>{u_path}'


if __name__ == '__main__':
    app.run(debug=True)