from flask import Flask

app = Flask(__name__)

@app.route("/about")
def about():
    return "<h1> This is the about page<h1/> " + "<h4> this is our official page .we are going to deal in flask <h4>"


if __name__ == '__main__':
    app.run(debug=True)