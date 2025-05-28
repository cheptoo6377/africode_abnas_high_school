from flask import Flask, request,jsonify


app = Flask(__name__)


@app.route('/divide')
def divide():
    string_arg = (request.args.get('num'))
    if not string_arg:
        return "please provide a number'num'", 400
    try:
        num = (string_arg)
        if num == 0:
            return "cannot divide by zero", 400

        return f"Result: {100 / num}" 
    except ValueError:
        return "invalid number format ",400


@app.route('/length')
def length():
    name = request.args.get('name')
    if not name:
        return "no name provided 'name'",400


    return f"Length: {len(name)}"  


@app.route('/add')
def add():
    a = request.args.get('a')  
    b = request.args.get('b')
    if not a or not b:
        return "please provide 'a'  and 'b'",400

    return f"Sum: {a + b}"  


@app.route('/undefined')
def undefined():
    value = request.args.get('value')

    return f"The value is: {value}"  


@app.route('/index')
def index():
    data = [1, 2, 3]
    i = request.args.get('i')
    if not i:
        return "please provide an index 'i'", 400
    return f"Item: {data[i] }"





@app.route('/submit', methods=['GET'])
def submit():
    data = request.args.get('data')
    if not data:
        return "please provide 'data'", 400
    return f"Received: {data}"

@app.route('/call')
def call():
    missing_function = request.args.get('missing_function')
    if not missing_function:
        return "please provide 'missing_function'", 400
    return missing_function()  


@app.route('/check-age')
def check_age():
    age = request.args.get('age')
    if not age:
        return "please provide 'age'", 400

    if age < 18:
        return "You are underage."
    elif age > 18:
        return "You are an adult."
    else:
        return "Age is unknown?"  

if __name__ == '__main__':
    app.run(debug=True)