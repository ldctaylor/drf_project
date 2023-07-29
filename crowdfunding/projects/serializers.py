from rest_framework import serializers
from django.apps import apps

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('projects.Condition')
        fields = '__all__'

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('projects.Pledge')
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    class Meta:
        model = apps.get_model('projects.Project')
        fields = '__all__'


