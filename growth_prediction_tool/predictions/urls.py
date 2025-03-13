from django.urls import path
from .views import SubmitPredictionView, PredictionHistoryView, RegisterView, UserProfileView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('submit-prediction/', SubmitPredictionView.as_view(), name='submit_prediction'),
    path('prediction-history/', PredictionHistoryView.as_view(), name='prediction_history'),
    path('user-profile/', UserProfileView.as_view(), name='user_profile'),
]