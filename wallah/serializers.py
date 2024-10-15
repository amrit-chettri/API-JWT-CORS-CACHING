from rest_framework import serializers
from .models import Lead
from django.contrib.auth.models import User

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'country' ,'email', 'message')

