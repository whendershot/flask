from flask import Flask, render_template

app = Flask(__name__.split('.')[0])

@app.route('/play')
@app.route('/play/<int:x>')
@app.route('/play/<int:x>/<string:color>')
def render_play(x:int = 3, color:str = 'blue'):
    return render_template('play.html', x = x, color = color)

@app.route('/', defaults={'u_path' : ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
    print(repr(u_path))
    return f'Sorry! No response. Try again. But how did you fall into here?<br>{u_path}'

if __name__ == '__main__':
    app.run(debug=True)