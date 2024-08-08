from flask_restful import Resource, reqparse, Api
from .models import db, Campaign
from datetime import datetime
from flask import jsonify

api = Api()

# Request parser
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help="Name cannot be blank!")
parser.add_argument('description', type=str, required=True, help="Description cannot be blank!")
parser.add_argument('start_date', type=lambda x: datetime.strptime(x, '%Y-%m-%d'), required=True, help="Start date cannot be blank! Format: YYYY-MM-DD")
parser.add_argument('end_date', type=lambda x: datetime.strptime(x, '%Y-%m-%d'), required=True, help="End date cannot be blank! Format: YYYY-MM-DD")
parser.add_argument('budget', type=float, required=True, help="Budget cannot be blank!")
parser.add_argument('visibility', type=str, required=True, choices=('PUBLIC', 'PRIVATE'), help="Visibility must be 'PUBLIC' or 'PRIVATE'")
parser.add_argument('goals', type=str) 

# Campaign Resource
class CampaignResource(Resource):
    def get(self, campaign_id):
        campaign = Campaign.query.get_or_404(campaign_id)
        return jsonify({
            'id': campaign.id,
            'name': campaign.name,
            'description': campaign.description,
            'start_date': campaign.start_date.strftime('%Y-%m-%d'),
            'end_date': campaign.end_date.strftime('%Y-%m-%d'),
            'budget': campaign.budget,
            'visibility': campaign.visibility,
            'goals': campaign.goals
        })

    def put(self, campaign_id):
        args = parser.parse_args()
        campaign = Campaign.query.get_or_404(campaign_id)
        campaign.name = args['name']
        campaign.description = args['description']
        campaign.start_date = args['start_date']
        campaign.end_date = args['end_date']
        campaign.budget = args['budget']
        campaign.visibility = args['visibility']
        campaign.goals = args.get('goals')
        db.session.commit()
        return jsonify({'message': 'Campaign updated successfully'})

    def delete(self, campaign_id):
        campaign = Campaign.query.get_or_404(campaign_id)
        db.session.delete(campaign)
        db.session.commit()
        return jsonify({'message': 'Campaign deleted successfully'})

# Campaign List Resource
class CampaignListResource(Resource):
    def get(self):
        # campaigns = Campaign.query.all()
        # return jsonify([{
        #     'id': campaign.id,
        #     'name': campaign.name,
        #     'description': campaign.description,
        #     'start_date': campaign.start_date.strftime('%Y-%m-%d'),
        #     'end_date': campaign.end_date.strftime('%Y-%m-%d'),
        #     'budget': campaign.budget,
        #     'visibility': campaign.visibility,
        #     'goals': campaign.goals
        # } for campaign in campaigns])
        return {"message":"this is from campaign API"}

    def post(self):
        args = parser.parse_args()
        new_campaign = Campaign(**args)
        db.session.add(new_campaign)
        db.session.commit()
        return {'message': 'Campaign created successfully'}, 201

# Adding resources to the API
api.add_resource(CampaignListResource, '/campaigns')
api.add_resource(CampaignResource, '/campaigns/<int:campaign_id>')