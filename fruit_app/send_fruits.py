from django.http import HttpResponse, JsonResponse

fruits = [
    {"Name": "Apfel", "Gewicht": 150, "Farbe": "Rot"},
    {"Name": "Banane", "Gewicht": 120, "Farbe": "Gelb"},
    {"Name": "Orange", "Gewicht": 180, "Farbe": "Orange"},
    {"Name": "Kiwi", "Gewicht": 100, "Farbe": "Grün"},
    {"Name": "Traube", "Gewicht": 50, "Farbe": "Violett"}
]

def send_fruits(request):
    return JsonResponse(fruits)

def single_fruit(request, fruit_id):
    return JsonResponse(fruits[fruit_id])
