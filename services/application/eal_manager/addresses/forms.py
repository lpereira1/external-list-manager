from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from eal_manager.models import IPAddress 
import ipaddress

class CreateAddress(FlaskForm):
    address = StringField('Address', 
                            validators=[
                                DataRequired(),
                                Length(min=7, max=21) ])
    name = StringField('Description', validators=[ DataRequired(), Length(min=5, max=255)])
                                
    organization = StringField('Customer or Organization', validators=[ DataRequired(),
                                Length(min=2, max=140) ])
    creator_id = current_user
    
    submit = SubmitField('Create Address')

    def validate_address(self, addr):
        dup_ip = IPAddress.query.filter_by(address=addr.data).first()
        if dup_ip:
            raise ValidationError('Address already exists.')
        
        elif '/' in addr.data:
            try:
                ipaddress.ip_network(addr.data)
            except ValueError as e:
                if 'host bits set' in str(e):
                    raise ValidationError('You input a host IP with a mask for a network. Verify information')
                else:
                    raise ValidationError(e)
        else:
            try:
                ipaddress.ip_address(addr.data)
            except:
                raise ValidationError('Invalid CIDR address, please enter a valide CIDR network or host IP')
