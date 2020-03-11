from flask import current_app
from eal_manager import db, login_manager
from datetime import datetime
from flask_login import UserMixin, current_user
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# Creates Database Columns based on Models. There are user who create address and 
# those addresses are part of an organization.
# user_1 = User(email='l@l.com', password = 'test')
# UNIQUE constraint failed: user.image_file
# user_2 = User(email='lazaro.pereira@gmail.com', password='Lazaro1')


@login_manager.user_loader
def load_user(email_id):
    return User.query.get(int(email_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(140), nullable=False)
    last_name = db.Column(db.String(140), nullable=False)
    email = db.Column(db.String(140), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    addresses = db.relationship('IPAddress', backref='creator', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)



    def __repr__(self):
        return f'User("{self.email}", "{self.image_file}")'

class IPAddress(db.Model):   
    address_id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(30)) 
    name = db.Column(db.String(255))
    organization = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    
    def __repr__(self):
        return f'User("{self.address}","{self.name}", "{self.organization}", "{self.date_created})'