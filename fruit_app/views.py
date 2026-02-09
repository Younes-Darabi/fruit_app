from django.http import HttpResponse, JsonResponse
from .fruits_data import fruits

def home_page(request):
    return HttpResponse("Hallo Welt!")

def send_fruits(request):
    return JsonResponse(fruits, safe=False)

def single_fruit(request, fruit_id):
    return JsonResponse(fruits[fruit_id])