from flask import render_template, flash, redirect, url_for, request, Blueprint
from eal_manager.addresses.forms import CreateAddress
from eal_manager.models import User, IPAddress
from flask_login import current_user, login_required
from eal_manager import db


addresses = Blueprint('addresses', __name__)


@addresses.route("/address/create", methods=['POST', 'GET'])
@login_required
def createaddress():
    form = CreateAddress()
    form.submit.label.text = 'Create Address'
    if form.validate_on_submit():
        address = IPAddress(address= form.address.data, 
                            name= form.name.data, 
                            organization=form.organization.data,
                            creator_id = current_user.first_name + ' ' + current_user.last_name )
        db.session.add(address)
        db.session.commit()
        flash(f'Whitelist updated with {form.address.data}!', 'success')
    return render_template('createaddress.html', title='startpage', form=form, legend='Create a new Address')


@addresses.route("/address/<int:addr_id>/update", methods=['POST', 'GET'])
@login_required
def update_addr(addr_id):
    address = IPAddress.query.get_or_404(addr_id)
    # Eventually we need to add a read and read/write permission here like
    # if address.creator_id.permissions != Write:
    #     abort(403)
    form = CreateAddress()
    form.submit.label.text = 'Update Address'

    
    if form.validate_on_submit():
        address.address = form.address.data
        address.name = form.name.data
        address.organization = form.organization.data
        address.creator_id = current_user.first_name + ' ' + current_user.last_name
        db.session.commit()
        flash('Address updated' , 'success')
        return redirect(url_for('main.startpage'))
    elif request.method == 'GET':
        form.address.data = address.address
        form.name.data = address.name
        form.organization.data = address.organization
        return render_template('createaddress.html', title='Update Address', 
                            form=form, legend='Update Address')

@addresses.route("/address/<int:addr_id>/delete", methods=['POST'])
@login_required
def delete_addr(addr_id):
    address = IPAddress.query.get_or_404(addr_id)
    db.session.delete(address)
    db.session.commit()
    flash('Address Deleted' , 'success')
    return redirect(url_for('main.startpage'))
