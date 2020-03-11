from flask import render_template, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from eal_manager.models import IPAddress

main = Blueprint('main', __name__)


@main.route("/")
@login_required
def startpage():
    page = request.args.get('page', 1, type=int)
    whitelisted_addresses = IPAddress.query.order_by(IPAddress.date_created.desc()).paginate(page=page, per_page=20)
    return render_template('index.html', whitelisted_addresses=whitelisted_addresses)

@main.route("/about")
@login_required
def about():
    return render_template('about.html', title='About')

