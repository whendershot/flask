from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!  Flask is interesting.'

@app.route('/success')
def sucess():
    return 'Success! Sucess! Success! Success! Success!'

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return f'Hello, {name}'

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return f'Username: {username}, ID: {id}'

if __name__ == '__main__':
    app.run(debug=True)