from database import db

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(120), unique=True)
    
    def __init__(self, brand, email,id):
        self.brand = brand
        self.email = email
        self.id = id
		
    def __repr__(self):
        return '<User %r>' % self.brand
		
		
class Component(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    component = db.Column(db.String(80), unique=True)
    account_id = db.Column(db.Integer, unique=False)
	
    def __init__(self, component,account_id,id):
		self.component = component
		self.account_id = account_id
		self.id = id
		
    def __repr__(self):
        return '<User %r>' % self.component
		
		
class Combination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    combination = db.Column(db.String(20), unique=True)
    wanted = db.Column(db.Integer,unique=False)
    account_id = db.Column(db.Integer, unique=False)
    
    def __init__(self, combination, wanted,account_id, id):
		self.combination = combination
		self.wanted = wanted
		self.account_id = account_id
		self.id = id
		
    def __repr__(self):
        return '<User %r>' % self.combination