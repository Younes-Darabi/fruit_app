from django.contrib import admin
from django.urls import path
from fruit_app.views import home_page, send_fruits, single_fruit

urlpatterns = [
    path('', home_page),
    path('fruits/', send_fruits),
    path('fruits/<int:fruit_id>', single_fruit)
]
