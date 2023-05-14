from flask import Flask, session
from app import app
from auth.authz import admin_role_required

def test_admin_role_required_decorator():

    with app.test_client() as client:
        # Make a request to the protected route without being an admin
        with client.session_transaction() as sess:
            sess["user_role_id"] = 2  # Set a non-admin role

        response = client.get("/test_admin_role_required", follow_redirects=True)
        assert response.status_code == 200
        print(response.get_data(as_text=True))
        assert b"You do not have permission to view that page." in response.data  # Expect a flash message

        # Make a request to the protected route as an admin
        with client.session_transaction() as sess:
            sess["user_role_id"] = 1  # Set an admin role

        response = client.get("/test_admin_role_required", follow_redirects=True)
        assert response.status_code == 200
        assert response.get_data(as_text=True) == "You are an admin!"  # Expect the correct content to be returned
        session.clear()
