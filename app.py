from flask import Flask, request, render_template, session, redirect
from auth.auth import login_required
app = Flask(__name__)

import controllers.questionnaire_controller
import controllers.auth_controller
import controllers.mentor_controller
import controllers.mentoring_categories_controller
@app.route("/")  # Same as @app.get('/') in flask 2
@login_required
def index():
    return render_template("dashboard.html", session=session)

@app.route("/force-login")
def force_login():
    session["userid"] = 1
    return redirect("/")


# This is required to use sessions.
app.secret_key = "lkjlhjjkhkhilhuih78hyioy89yt9o8t87tr"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)  # pragma; no coverage