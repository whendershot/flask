from flask import Flask, render_template, request, redirect, session

app = Flask(__name__.split('.')[0])
app.secret_key = 'Something randomly generated, with a one1!.'

@app.route('/', methods=['POST'])
def posting_index():
    print(request)
    if 'visit_counter_string' in session:
        session['visit_counter'] += int(request.form['add_to_visit_counter']) - 1
        session['visit_counter_string'] = f'You have visited {session["visit_counter"]} times!'
    else:
        session['visit_counter'] = int(request.form['add_to_visit_counter']) - 1
        session['visit_counter_string'] = f'This is your first visit.  Welcome!'
    
    if 'hidden_visit_counter' in session:
        session['hidden_visit_counter'] += int(request.form['add_to_visit_counter']) - 1
    else:
        session['hidden_visit_counter'] = int(request.form['add_to_visit_counter']) - 1

    return redirect('/')

@app.route('/')
def my_index():
    if 'visit_counter_string' in session:
        session['visit_counter'] += 1
        session['visit_counter_string'] = f'You have visited {session["visit_counter"]} times!'
    else:
        session['visit_counter'] = 1
        session['visit_counter_string'] = f'This is your first visit.  Welcome!'

    if 'hidden_visit_counter' in session:
        session['hidden_visit_counter'] += 1
    else:
        session['hidden_visit_counter'] = 1
    
    print(f"Total visits: {session['hidden_visit_counter']}")
    print(f"Regular visits: {session['visit_counter']}")
    return render_template('./index.html')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    #erase the session information.
    session.pop('visit_counter')
    session.pop('visit_counter_string')
    return redirect('/')

@app.route('/', defaults={'u_path' : ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
    print(repr(u_path))
    return f'Sorry! No response. Try again. But how did you fall into here?<br>{u_path}'


if __name__ == '__main__':
    app.run(debug=True)