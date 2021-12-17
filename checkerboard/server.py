from flask import Flask, render_template

app = Flask(__name__.split('.')[0])

@app.route('/')
@app.route('/<int:row>')
@app.route('/<int:row>/<int:col>')
@app.route('/<int:row>/<int:col>/<string:color1>')
@app.route('/<int:row>/<int:col>/<string:color1>/<string:color2>')
def serve_checkerboard(col:int = 8, row:int = 8, color1:str = "black", color2:str = "red"):
    return render_template('checkerboard.html', col=col, row=row, color1=color1, color2=color2)

@app.route('/', defaults={'u_path' : ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
    print(repr(u_path))
    return f'Sorry! No response. Try again. But how did you fall into here?<br>{u_path}'


if __name__ == '__main__':
    app.run(debug=True)