from rest_framework import serializers
from .models import Analyses


class AnalysesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analyses
        fields = '__all__'
