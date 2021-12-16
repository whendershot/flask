from re import UNICODE
from flask import Flask

app = Flask(__name__.split('.')[0])

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say(name):
    return f'Hi, {name}'

@app.route('/repeat/<int:number>/<string:word>')
def repeat(number, word):
    return f'{word}<br>' * int(number)

@app.route('/', defaults={'u_path' : ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
    print(repr(u_path))
    return 'Sorry! No response. Try again.'

if __name__ == '__main__':
    app.run(debug=True)