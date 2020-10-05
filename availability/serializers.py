from rest_framework import serializers
from .models import *
from provider.models import  Provider
from collections import defaultdict
from service.models import Category, Service
from .models import Availability



class AvailabilitySerializer(serializers.Serializer):
	days = (
		('monday', 'm'),
		('tuesday', 't'),
		('wednesday', 'w'),
		('thursday', 'th'),
		('friday', 'f'),
		('saturday', 's'),
		('sunday', 'su'),
	)
	id=serializers.ReadOnlyField()
	day = serializers.ChoiceField(choices=days, required=False)
	begin = serializers.TimeField()
	end = serializers.TimeField()
	is_break = serializers.BooleanField(required=False)
	is_working = serializers.BooleanField(required=False, default=True)
	provider = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all(), many=False, required=False)


	def create(self, validated_data):
		availability = Availability.objects.create(**validated_data)
		availability.save()
		return availability

	# def validate(self, attrs):
	# 	errors =defaultdict(list)
	# 	provider = attrs['provider']
	# 	day = attrs['day']
	# 	day_qs = Week.objects.filter(provider=provider, day=day).first()
	# 	if not self.instance and provider and day_qs:
	# 		errors['user'].append('Already registered.')
	# 	if errors:
	# 		raise serializers.ValidationError(errors)

	# 	return attrs

	def update(self, instance, validated_data):
		instance.day = validated_data.get('day', instance.day)
		instance.begin = validated_data.get('begin', instance.begin)
		instance.end = validated_data.get('end', instance.end)
		instance.is_break = validated_data.get('is_break', instance.is_break)
		instance.save()
		return instance




class UpdateWorkingDaySerializer(serializers.Serializer):
	id=serializers.ReadOnlyField()
	is_working = serializers.BooleanField(required=False, default=True)

	def update(self, instance, validated_data):
		instance.is_working = validated_data.get('is_working', instance.is_working)
		instance.save()
		return instance


class AddBreakSerializer(serializers.Serializer):
	id=serializers.ReadOnlyField()
	begin = serializers.TimeField()
	end = serializers.TimeField()

	def update(self, instance, validated_data):
		instance.begin = validated_data.get('begin', instance.begin)
		instance.end = validated_data.get('end', instance.end)
		instance.is_break = True
		instance.save()
		return instance






