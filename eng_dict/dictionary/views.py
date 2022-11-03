from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import *


class DictionaryAPIView(generics.ListCreateAPIView):
    queryset = Dictionary.objects.all()
    serializer_class = dictionarySerializers


class DictionaryUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dictionary.objects.all()
    serializer_class = dictionarySerializers
