from rest_framework import serializers
from catalog.models import *
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' 