from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from score_calculator.models import RecipeInput
from serializers import RecipeInputSerializer
from score_calculator import score


def index(request):
    return HttpResponse("Hello World")

@csrf_exempt
def get_score(request):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        recipe_data = RecipeInput(request_data)
        prediction = score.score(recipe_data)
        return JsonResponse({'predicted_score': prediction[0]})

    else:
        return JsonResponse({'error': 'Invalid Request Type (Use POST)'})
