from rest_framework import serializers
from django.apps import apps
from .models import Project, Pledge, Condition

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    class Meta:
        model = Pledge
        fields = '__all__'

class PledgeDetailSerializer(PledgeSerializer):
    # How do I bring in the relevant project's detail, here????????????????

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount',instance.amount)
        instance.comment = validated_data.get('comment',instance.comment)
        instance.pledge_date = validated_data.get('pledge_date',instance.pledge_date)
        instance.project = validated_data.get('project',instance.project)
        instance.supporter = validated_data.get('supporter',instance.supporter)
        instance.condition = validated_data.get('condition',instance.condition)
        instance.save()
        return instance 


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Project
        fields = '__all__'

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal',instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.goaldate = validated_data.get('goaldate', instance.goaldate)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance


