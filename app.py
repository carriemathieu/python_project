from flask import Flask, render_template, request, redirect, url_for
from forms import Todo

# creates instance of flask & assigns to app var
app = Flask(__name__)

# protects against CSRF
app.config['SECRET_KEY'] = 'password'

# get and post requests
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_method = request.method
    if request_method == 'POST':
        # print outs data that was input in form
        first_name = request.form['first_name']
        # redirect to url for name
        return redirect(url_for('name', first_name=first_name))

    return render_template('hello.html', request_method=request_method)

@app.route('/name/<string:first_name>')
def name(first_name):
    return f'{first_name}'

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    todo_form = Todo()
    if todo_form.validate_on_submit()
        print(todo_form.content.data)
        return redirect('/')
    return render_template('todo.html', form=todo_form)

# if app.py is executed directly, run app (flask server)
if __name__ == '__main__':
    app.run(debug=True)