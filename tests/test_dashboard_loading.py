from flask import Flask, session
from app import app
def test_load_dashboard():

    with app.test_request_context():

        # Test the mentor dashboard template
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess["user_role_id"] = 2  # Set a non-admin role
                sess['userid'] = 1
            response = client.get("/", follow_redirects=True)
            assert b"View Proposed Matches" in response.data

        # Define a fake session with a user role ID of 1 (admin)
        session["user_role_id"] = 1

        # Test the admin dashboard template
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess["user_role_id"] = 1  # Set a admin role
                sess['userid'] = 1
            response = client.get("/", follow_redirects=True)
            assert b"Manage Admins" in response.data
        session.clear()