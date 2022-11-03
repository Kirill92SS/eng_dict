from rest_framework import serializers
from .models import *


class dictionarySerializers(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ('id', 'words',)
