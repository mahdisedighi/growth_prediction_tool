from pymongo import MongoClient

def get_mongo_client():
    connection_string ='mongodb://localhost:27017/growth?authSource=admin'
    client = MongoClient(connection_string)
    return client

def get_prediction_collection():
    client = get_mongo_client()
    db = client['growth']  # Use 'growth' database
    collection = db['growth']  # Use 'growth' collection for predictions
    return collection

def get_users_collection():
    client = get_mongo_client()
    db = client['growth']  # Use 'growth' database
    collection = db['users']  # Independent 'users' collection
    return collection


def generate_insights(input_data):
    insights = []
    
    # Revenue Growth
    if input_data['revenue_growth'] > 70:
        insights.append("Strong revenue growth indicates a healthy business.")
    elif input_data['revenue_growth'] < 30:
        insights.append("Low revenue growth may signal underlying issues.")
    
    # Market Share
    if input_data['market_share'] > 70:
        insights.append("High market share positions you well against competitors.")
    elif input_data['market_share'] < 30:
        insights.append("Low market share may limit your growth potential.")
    
    # Digital Engagement Score
    if input_data['digital_engagement_score'] > 70:
        insights.append("High digital engagement can drive customer acquisition.")
    elif input_data['digital_engagement_score'] < 30:
        insights.append("Improving digital engagement could enhance customer reach.")
    
    # Consumer Loyalty Score
    if input_data['consumer_loyalty_score'] > 70:
        insights.append("Strong consumer loyalty is a key asset.")
    elif input_data['consumer_loyalty_score'] < 30:
        insights.append("Low consumer loyalty may lead to higher churn rates.")
    
    # Marketing Budget Allocation
    if input_data['marketing_budget_allocation'] > 70:
        insights.append("Significant marketing investment may boost brand visibility.")
    elif input_data['marketing_budget_allocation'] < 30:
        insights.append("Limited marketing budget could hinder promotional efforts.")
    
    # Sustainability Index
    if input_data['sustainability_index'] > 70:
        insights.append("Strong sustainability practices can attract eco-conscious consumers.")
    elif input_data['sustainability_index'] < 30:
        insights.append("Improving sustainability could enhance brand reputation.")
    
    # E-commerce Market Share
    if input_data['e_commerce_market_share'] > 70:
        insights.append("Dominant e-commerce presence is advantageous in the digital age.")
    elif input_data['e_commerce_market_share'] < 30:
        insights.append("Expanding e-commerce capabilities could capture more online sales.")
    
    # Physical Retail Presence
    if input_data['physical_retail_presence'] > 70:
        insights.append("Extensive physical retail network provides broad accessibility.")
    elif input_data['physical_retail_presence'] < 30:
        insights.append("Limited physical retail may reduce customer touchpoints.")
    
    # Competition Level (note: lower is better)
    if input_data['competition_level'] < 30:
        insights.append("Low competition provides ample growth opportunities.")
    elif input_data['competition_level'] > 70:
        insights.append("High competition requires differentiation strategies.")
    
    return insights