from functools import wraps
from flask import request, redirect, url_for, session

def admin_role_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_role_id',0) != 1:
            return redirect(url_for('load_dashboard'))
        return f(*args, **kwargs)
    return decorated_function