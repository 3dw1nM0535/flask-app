from flask import render_template, abort
from flask_login import login_required, current_user

from . import home

@home.route("/")
def homepage():
	"""Render home page on / route
	"""
	return render_template("home/index.html", title="Welcome")

@home.route("/dashboard")
@login_required
def dashboard():
	"""Render dashboard page on / dashboard route
	"""
	return render_template("home/dashboard.html", title="Dashboard")

@home.route("/admin/dashboard")
@login_required
def admin_dashboard():
	"""
	Render dashboard page on /admin/dashboard route
	"""
	if not current_user.is_admin:
		abort(403)

	return render_template("home/admin_dashboard.html", title="Dashboard")
