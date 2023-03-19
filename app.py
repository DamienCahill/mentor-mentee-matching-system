from flask import Flask

app = Flask(__name__)

@app.route("/")  # Same as @app.get('/') in flask 2
def index():
    return "Hello Word"



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)  # pragma; no coverage