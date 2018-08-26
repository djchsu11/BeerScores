from rest_framework import serializers
from score_calculator.models import RecipeInput

class RecipeInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeInput
        fields = ('OG', 'FG', 'ABV', 'IBU', 'Color', 'BoilSize', 'BoilGravity', 'Efficiency', 'PrimaryTemp')
