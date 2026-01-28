from flask import Blueprint, render_template, request, redirect, url_for, make_response
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    target_date = request.cookies.get('target_date')

    if not target_date:
        target_date = "Jan 30, 2026 09:00:00"

    return render_template('index.html', target_date=target_date)


@main.route('/create', methods=['POST'])
def create_event():
    target_date = request.form.get('target_date')

    response = make_response(redirect(url_for('main.index')))
    response.set_cookie('target_date', target_date, max_age=60*60*24*365)  # 1 ano

    return response
