from flask import Flask

app = Flask(__name__)

@app.route("/")  # Same as @app.get('/') in flask 2
def index():
    return "Hello World"



if __name__ == "__main__":
    app.run(debug=True)  # pragma; no coverage