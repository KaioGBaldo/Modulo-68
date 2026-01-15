from django.urls import path
from .views import ViewProtegida

urlpatterns = [
    path("protegido/", ViewProtegida.as_view()),
]
