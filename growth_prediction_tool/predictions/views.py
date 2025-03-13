from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import get_prediction_collection, get_users_collection, generate_insights
from .ml_model import SuccessScoreModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import datetime
class SubmitPredictionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        required_fields = [
            'revenue_growth', 'market_share', 'digital_engagement_score',
            'consumer_loyalty_score', 'marketing_budget_allocation',
            'sustainability_index', 'e_commerce_market_share',
            'physical_retail_presence', 'competition_level'
        ]
        inputs = []
        for field in required_fields:
            try:
                inputs.append(float(data[field]))
            except (KeyError, ValueError):
                return Response({'error': f'Missing or invalid {field}'}, status=status.HTTP_400_BAD_REQUEST)

        model = SuccessScoreModel()
        success_score = model.predict(inputs)
        risk_level = 'low' if success_score > 80 else 'medium' if success_score > 60 else 'high'

        # Prepare input data dictionary for insights generation
        input_data = {field: float(data[field]) for field in required_fields}
        
        # Generate market insights
        insights = generate_insights(input_data)

        # Store prediction data including insights
        prediction_data = {
            'user_id': request.user.id,
            **input_data,
            'success_score': float(success_score),
            'risk_level': risk_level,
            'insights': insights,  # Add insights to the stored data
            'created_at': datetime.datetime.now(),
        }

        collection = get_prediction_collection()
        collection.insert_one(prediction_data)

        # Return success score, risk level, and insights in the response
        return Response({
            'success_score': success_score,
            'risk_level': risk_level,
            'insights': insights  # Include insights in the response
        }, status=status.HTTP_201_CREATED)
    
class PredictionHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        collection = get_prediction_collection()  # Points to 'growth' collection in 'growth' database
        predictions = collection.find({'user_id': request.user.id})
        predictions_list = [{**pred, '_id': str(pred['_id']), 'created_at': pred['created_at'].isoformat()} for pred in predictions]
        return Response(predictions_list)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create user in Django's auth system (SQLite)
        user = User.objects.create_user(username=username, password=password)
        
        # Store additional user data in MongoDB 'users' collection
        users_collection = get_users_collection()  # Points to 'users' collection in 'growth' database
        users_collection.insert_one({
            'user_id': user.id,
            'username': username,
            'created_at': datetime.datetime.now()
        })

        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        collection = get_users_collection()  # Points to 'users' collection in 'growth' database
        user_data = collection.find_one({'user_id': request.user.id})
        if user_data:
            user_data['_id'] = str(user_data['_id'])
            user_data['created_at'] = user_data['created_at'].isoformat()
        return Response(user_data or {})

    def post(self, request):
        collection = get_users_collection()  # Points to 'users' collection in 'growth' database
        data = request.data
        data['user_id'] = request.user.id
        collection.update_one({'user_id': request.user.id}, {'$set': data}, upsert=True)
        return Response({'message': 'Profile updated'}, status=status.HTTP_200_OK)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate user using Django's built-in authentication
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }, status=status.HTTP_200_OK)