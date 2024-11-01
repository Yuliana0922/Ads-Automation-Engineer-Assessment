import json
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.ad import Ad
from datetime import datetime, timedelta

# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Setting up credentials
credentials = config["credentials"]
my_app_id = credentials["app_id"]
my_app_secret = credentials["app_secret"]
my_access_token = credentials["access_token"]

# Initializing API
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
ad_account = AdAccount(config["ad_account_id"])

# Defining time variables
start_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
end_time = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%S')

# Creating Campaign
campaign_details = config["campaign_details"]
campaign = ad_account.create_campaign(params={
    'name': campaign_details["name"],
    'objective': campaign_details["objective"],  
    'status': campaign_details["status"],
    'special_ad_categories': campaign_details["special_ad_categories"],
})

print(f"Campaign created with ID: {campaign['id']}")

# Create Ad Set
ad_set_details = config["ad_set_details"]
ad_set = ad_account.create_ad_set(params={
    'name': ad_set_details["name"],
    'campaign_id': campaign['id'],
    'daily_budget': ad_set_details["daily_budget"],
    'billing_event': ad_set_details["billing_event"],
    'optimization_goal': ad_set_details["optimization_goal"],
    "bid_strategy": ad_set_details["bid_strategy"],
    "bid_amount": ad_set_details["bid_amount"],
    "bid_cap": ad_set_details["bid_cap"],
    'targeting': ad_set_details["targeting"],
    'status': ad_set_details["status"],
    'start_time': start_time,
    'end_time': end_time,    
})

print(f"Ad Set created with ID: {ad_set['id']}")

# Ad Creative
ad_creative_details = config["ad_creative_details"]
ad_creative = ad_account.create_ad_creative(params={
    'name': ad_creative_details["name"],
    'object_story_spec': {
        'page_id': ad_creative_details["page_id"],
        'link_data': ad_creative_details["link_data"]
    },
})

print(f"Ad Creative created with ID: {ad_creative['id']}")

# Create Ad
ad = ad_account.create_ad(params={
    'name': 'Job Post Ad',
    'adset_id': ad_set['id'],
    'creative': {'creative_id': ad_creative['id']},
    'status': 'PAUSED',
})

print(f"Ad created with ID: {ad['id']}")

insights = ad_account.get_insights(params={
    'level': 'ad',
    'fields': ['impressions', 'reach', 'clicks', 'ctr'],
})
print(insights)
