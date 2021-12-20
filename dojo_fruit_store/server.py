from flask import Flask, render_template, request, redirect, session
from datetime import datetime, timezone

app = Flask(__name__.split('.')[0])
app.secret_key = 'Insert movie reference here...'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    form = request.form
    num_fruits = int(form['apple']) + int(form['strawberry']) + int(form['raspberry']) + int(form['blackberry'])
    session['last_checkout'] = request.form
    session['num_fruits'] = num_fruits
    session['submission_timestamp'] = datetime.now(timezone.utc)
    print(f'Charging {form["first_name"] + " " + form["last_name"]} for {num_fruits} fruits.')
    #handle the purchase request
    return redirect("/checked_out")

@app.route('/checked_out')
def post_checkout():
    print(f"In the post checkout phase: {session['last_checkout']}")
    return render_template("checkout.html", cart_info=session['last_checkout'])


@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

@app.route('/', defaults={'u_path' : ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
    print(repr(u_path))
    return f'Sorry! No response. Try again. But how did you fall into here?<br>{u_path}'


if __name__=="__main__":   
    app.run(debug=True)    