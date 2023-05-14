from flask import Flask, session
from app import app
from auth.auth import login_required

def test_login_required_decorator():

    @app.route("/testing")
    @login_required
    def login_req():
        return "You are logged in!"

    with app.test_client() as client:
        # Make a request to the protected route without logging in
        response = client.get("/testing")
        assert response.status_code == 302  # Expect a redirect to the login page

        # Log in by setting the session variable
        with client.session_transaction() as sess:
            sess["userid"] = "123"

        # Make a request to the protected route after logging in
        response = client.get("/testing")
        assert response.status_code == 200  # Expect a successful response
        assert response.get_data(as_text=True) == "You are logged in!"  # Expect the correct content to be returned
        session.clear()

