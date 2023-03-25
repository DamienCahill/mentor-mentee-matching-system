from functools import wraps
from flask import request, redirect, url_for, session

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("userid",0):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function