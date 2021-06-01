from flask import Flask

# creates instance of flask & assigns to app var
app = Flask(__name__)

# function that returns 'hello world'
@app.route('/')
def hello_world():
    return "<h1>Hello world</h1>"

# if app.py is executed directly, run app (flask server)
if __name__ == '__main__':
    app.run(debug=True)