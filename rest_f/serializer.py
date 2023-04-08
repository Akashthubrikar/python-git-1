from rest_framework import serializers
from . import models


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.cast
        fields= ["id","name","school"]