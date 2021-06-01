# render_template must be imported to render html templates
from flask import Flask, render_template

app = Flask(__name__)

# renders hello.html template, passes in list_of_names as property
# in HTML file: {% =%} Jinja, allows writing code similar to python syntax
@app.route('/')
def index():
    return render_template('hello.html', list_of_names=['x', 'y', 'z'])

# accepts a name as url params, and returns "hello (name)"
@app.route('/<string:name>')
def greet(name):
    return f'Hello {name}'

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)