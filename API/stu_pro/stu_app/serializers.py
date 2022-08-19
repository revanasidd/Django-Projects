from rest_framework import serializers
from .models import Stu_details

class Stu_serializer(serializers.ModelSerializer):
    class Meta:
        model=Stu_details
        fields='__all__'