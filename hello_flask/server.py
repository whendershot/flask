from flask import Flask, render_template, request, redirect

app = Flask(__name__.split('.')[0])
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/form_post')
def test_form_post():
    return render_template('form_post.html')

@app.route('/form_post/users', methods=['POST'])
def test_handle_users():
    #Never use a render template on POST.
    print('Got some post info!')
    print(request.form)
    return redirect('/form_post')

@app.route('/static')
def render_static():
    return render_template('static.html')

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

@app.route('/lists/hard_coded')
def render_lists_hard_coded():
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("./lists.html", random_numbers = [3,1,5], students = student_info)

@app.route('/', defaults={'u_path' : ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
    print(repr(u_path))
    return f'Sorry! No response. Try again. But how did you fall into here?<br>{u_path}'


if __name__ == '__main__':
    app.run(debug=True)