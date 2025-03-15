from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    Model to store additional user profile data.
    Uses a OneToOneField to link with the built-in User model and a JSONField for flexible data storage.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data = models.JSONField(default=dict, help_text="Stores arbitrary user profile data as JSON")

    class Meta:
        db_table = "users"


    def __str__(self):
        return f"Profile of {self.user.username}"



class Prediction(models.Model):
    """
    Model to store prediction data submitted by users.
    Includes all fields from SubmitPredictionView and links to the User model.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="The user who submitted the prediction")
    revenue_growth = models.FloatField(help_text="Revenue growth percentage")
    market_share = models.FloatField(help_text="Market share percentage")
    digital_engagement_score = models.FloatField(help_text="Score for digital engagement")
    consumer_loyalty_score = models.FloatField(help_text="Score for consumer loyalty")
    marketing_budget_allocation = models.FloatField(help_text="Marketing budget allocation percentage")
    sustainability_index = models.FloatField(help_text="Sustainability performance index")
    e_commerce_market_share = models.FloatField(help_text="E-commerce market share percentage")
    physical_retail_presence = models.FloatField(help_text="Physical retail presence score")
    competition_level = models.FloatField(help_text="Level of market competition")
    success_score = models.FloatField(help_text="Calculated success score")
    risk_level = models.CharField(
        max_length=10,
        choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
        help_text="Risk level based on success score"
    )
    insights = models.JSONField(help_text="List of market insights as JSON")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp of prediction creation")

    class Meta:
        db_table = "growth"

    def __str__(self):
        return f"Prediction for {self.user.username} at {self.created_at}"