from flask import Flask, request, render_template, session, redirect, Blueprint
from auth.auth import login_required
from controllers.dashboard_controller import dashboard_controller_bp
from controllers.questionnaire_controller import questionnaire_controller_bp
from controllers.auth_controller import auth_controller_bp
from controllers.mentor_controller import mentor_controller_bp
from controllers.mentoring_categories_controller import  mentoring_categories_controller_bp
from controllers.matches_controller import matches_controller_bp
from controllers.admin_controller import admin_controller_bp

app = Flask(__name__)
app.debug = True
with app.app_context():
    app.register_blueprint(dashboard_controller_bp)
    app.register_blueprint(questionnaire_controller_bp)
    app.register_blueprint(auth_controller_bp)
    app.register_blueprint(mentor_controller_bp)
    app.register_blueprint(mentoring_categories_controller_bp)
    app.register_blueprint(matches_controller_bp)
    app.register_blueprint(admin_controller_bp)
# This is required to use sessions.
app.secret_key = "lkjlhjjkhkhilhuih78hyioy89yt9o8t87tr"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)  # pragma; no coverage