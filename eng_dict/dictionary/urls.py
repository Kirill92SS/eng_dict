from django.urls import path, include
from .views import *

urlpatterns = [
    path('dict/', DictionaryAPIView.as_view()),
    path('dict/<int:pk>/', DictionaryUDAPIView.as_view()),
]
