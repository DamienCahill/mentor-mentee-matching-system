from flask import Blueprint
from auth.authz import admin_role_required

fixtures_bp = Blueprint('fixtures_bp',__name__)
@fixtures_bp.route("/test_admin_role_required")
@admin_role_required
def admin_req():
    return "You are an admin!"