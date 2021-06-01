from flask import Flask, render_template, request, redirect, url_for

# creates instance of flask & assigns to app var
app = Flask(__name__)

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

# if app.py is executed directly, run app (flask server)
if __name__ == '__main__':
    app.run(debug=True)