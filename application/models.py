from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(100))
    industry = db.Column(db.String(100))  
    budget = db.Column(db.Float)  
    category = db.Column(db.String(100)) 
    niche = db.Column(db.String(100)) 
    reach = db.Column(db.Float) 
    role_id = db.Column(db.String(20), db.ForeignKey('role.id'))  # 'admin', 'sponsor', 'influencer'
    role = db.relationship('Role')

    def __repr__(self):
        return f'<User {self.username}>'
    
class Role(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return f'<Role {self.name}>'

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    budget = db.Column(db.Float, nullable=False)
    visibility = db.Column(db.String(20), nullable=False)  # 'public' or 'private'
    goals = db.Column(db.Text)

    ad_requests = db.relationship('AdRequest', backref='campaign', lazy=True)

    def __repr__(self):
        return f'<Campaign {self.name}>'
    
class AdRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
    influencer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    messages = db.Column(db.Text)
    requirements = db.Column(db.Text)
    payment_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # 'Pending', 'Accepted', 'Rejected'

    def __repr__(self):
        return f'<AdRequest {self.id}>'
    

class Statistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    active_users = db.Column(db.Integer)
    campaigns_count = db.Column(db.Integer)
    public_campaigns_count = db.Column(db.Integer)
    private_campaigns_count = db.Column(db.Integer)
    ad_requests_count = db.Column(db.Integer)
    flagged_sponsors_count = db.Column(db.Integer)
    flagged_influencers_count = db.Column(db.Integer)

    def __repr__(self):
        return f'<Statistics {self.id}>'