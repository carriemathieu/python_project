from flask import Flask

app = Flask(__name__)

# accepts a name as url params, and returns "hello (name)"
@app.route('/<name>')
def greet(name):
    return f'Hello {name}'

if __name__ == '__main__':
    app.run(debug=True)