from flask import Flask, render_template, request, redirect, url_for
from forms import Todo
from flask_sqlalchemy import SQLAlchemy

# creates instance of flask & assigns to app var
app = Flask(__name__)

# protects against CSRF
app.config['SECRET_KEY'] = 'password'
# sets up SQLAlchemy DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
# creates instance of DB
db = SQLAlchemy(app)

class TodoModel(db.Model):
    # creates column in DB for ID
    id = db.Column(db.Integer, primary_key=True)
    # 240 characters allowed for content
    content = db.Column(db.String(240))

    # return string representation of model
    def __str__(self):
        return f'{self.content}, {self.id}'

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
    if todo_form.validate_on_submit():
        print(todo_form.content.data)
        return redirect('/')
    return render_template('todo.html', form=todo_form)

# if app.py is executed directly, run app (flask server)
if __name__ == '__main__':
    app.run(debug=True)