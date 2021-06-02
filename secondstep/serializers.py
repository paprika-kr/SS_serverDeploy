from rest_framework import serializers
from .models import Object

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ('title_kor', 'title_eng', 'illust')