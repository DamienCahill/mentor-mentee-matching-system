from flask import Flask, request, render_template, session, redirect
from auth.auth import login_required
app = Flask(__name__)

import controllers.questionnaire_controller
import controllers.auth_controller
import controllers.mentor_controller
import controllers.mentoring_categories_controller
import controllers.dashboard_controller
import controllers.admin_controller
import controllers.matches_controller
# This is required to use sessions.
app.secret_key = "lkjlhjjkhkhilhuih78hyioy89yt9o8t87tr"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)  # pragma; no coverage