from rest_framework import serializers
from .models import Helpers

class HelpersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helpers
        fields = '__all__'