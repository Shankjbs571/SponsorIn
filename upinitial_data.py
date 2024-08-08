from app import app
from application.models import db, Role

with app.app_context():
    db.create_all()
    admin_role = Role(id='admin',name='ADMIN',description='This is Admin Role')
    sponsor_role = Role(id='sponsor',name='SPONSOR',description='This is Sponsor Role')
    influencer_role = Role(id='influencer',name='INFLUENCER',description='This is Influencer Role')

    db.session.add(admin_role)
    db.session.add(sponsor_role)
    db.session.add(influencer_role)
    db.session.commit()

