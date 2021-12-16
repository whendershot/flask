from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/repeater')
def index():
    return render_template('repeater.html', phrase='hello', times=5)

@app.route('/success')
def sucess():
    return 'Success! Sucess! Success! Success! Success!'

@app.route('/hello/<string:name>')
def hello(name:str):
    print(name)
    return f'Hello, {name}'

@app.route('/users/<string:username>/<int:id>')
def show_user_profile(username:str, id:int):
    print(username)
    print(id)
    return f'Username: {username}, ID: {id}'

@app.route('/', defaults={'u_path' : ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
    print(repr(u_path))
    return f'Sorry! No response. Try again. But how did you fall into here?<br>{u_path}'


if __name__ == '__main__':
    app.run(debug=True)