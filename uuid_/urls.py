from .views import UUIDGenerator
from django.urls import path

urlpatterns = [
    path('generate-uuid/', UUIDGenerator.as_view()),
]
