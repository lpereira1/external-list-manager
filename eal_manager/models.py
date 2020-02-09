from eal_manager import db 
from datetime import datetime


# Creates Database Columns based on Models. There are user who create address and 
# those addresses are part of an organization.
# user_1 = User(email='l@l.com', password = 'test')
# UNIQUE constraint failed: user.image_file
# user_2 = User(email='lazaro.pereira@gmail.com', password='Lazaro1')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(140), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    addresses = db.relationship('IPAddress', backref='creator', lazy=True)

    def __repr__(self):
        return f'User("{self.email}", "{self.image_file}")'

class IPAddress(db.Model):   
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(20)) 
    name = db.Column(db.String(255))
    organization = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False )
    
    def __repr__(self):
        return f'User("{self.address}","{self.name}", "{self.organization}", "{self.date_created})'