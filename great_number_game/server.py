from flask import Flask, render_template, request, redirect, session
import random


app = Flask(__name__.split('.')[0])
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def game_frame():
    print(session)
    if ('playing_game' in session and (session['playing_game'] or session['guess_class'] != None)):
        return render_template('./guess.html')
    else :
        session['playing_game'] = True
        session['secret_number'] = str(random.randint(1, 100))
        session['num_guesses'] = 0
        return render_template('./number_game.html')

@app.route('/make_guess', methods=['POST'])
def play_round():
    print(f"Session: {session}")
    print(f"Request: {request.form}")
    if ('playing_game' in session) and (session['playing_game']):
        session['current_guess'] = request.form['guess']
        session['num_guesses'] += 1
        if session['current_guess'] == session['secret_number']:
            session['result_string'] = f"{session['current_guess']} was the correct number!  You used {session['num_guesses']} guesses."
            session['playing_game'] = False
            session['guess_class'] = 'success'
        elif session['num_guesses'] >=5:
            session['playing_game'] = False
            session['guess_class'] = 'failure'
            session['result_string'] = f"You failed to guess within 5 guesses.  {session['secret_number']} was the correct number.  Try again?"
        elif session['current_guess'] < session['secret_number']:
            session['result_string'] = f"{session['current_guess']} is too low!"
            session['guess_class'] = 'failure'
        else:
            session['result_string'] = f"{session['current_guess']} is too high!"
            session['guess_class'] = 'failure'

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/', defaults={'u_path' : ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
    print(repr(u_path))
    return f'Sorry! No response. Try again. But how did you fall into here?<br>{u_path}'


if __name__ == '__main__':
    app.run(debug=True)