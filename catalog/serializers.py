from rest_framework import serializers
from .models import *
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' 