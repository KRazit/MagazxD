from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    salary = serializers.IntegerField(default=25000)
    company = serializers.CharField(max_length=25)