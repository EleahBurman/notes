from flask import Blueprint, render_template

views = Blueprint('views', __name__)
from flask_login import login_user, login_required, logout_user, current_user


@views.route('/')
@login_required
def home():
  return render_template("home.html")
