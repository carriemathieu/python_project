from flask import Flask, render_template, request

# creates instance of flask & assigns to app var
app = Flask(__name__)

# get and post requests
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_method = request.method
    return render_template('hello.html', request_method=request_method)

# if app.py is executed directly, run app (flask server)
if __name__ == '__main__':
    app.run(debug=True)