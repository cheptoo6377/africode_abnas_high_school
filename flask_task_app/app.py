from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return " <h1>welcome to  task app <h1/>"

@app.route("/tasks")
def task():
    return "this is the task list app"

if __name__ == '__main__':
    app.run(debug=True)