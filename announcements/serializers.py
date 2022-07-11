from rest_framework import serializers
from announcements.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email','password','test']

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id','name']


class TestSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Test2
        fields = ['id', 'name']


