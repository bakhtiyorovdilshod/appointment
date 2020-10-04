from rest_framework import serializers
from django.contrib.auth import get_user_model
from service.models import Service
from availability.models import Availability
from user.models import Contact
from provider.models import Provider
from collections import defaultdict
from service.models import Service
from service.serializers import ServiceSerializer
User = get_user_model()


class ProviderSerializer(serializers.Serializer):
	genders = (
		('male', 'male'),
		('female', 'female')
	)
	id=serializers.ReadOnlyField()
	user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
	first_name = serializers.CharField(max_length=200, required=False)
	last_name = serializers.CharField(max_length=200, required=False)
	address = serializers.CharField(max_length=200, required=False)
	gender = serializers.ChoiceField(choices=genders, required=False)
	rate = serializers.IntegerField(default=0,required=False)
	services = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True, required=False)
	# contact = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all(),many=True, required=False)


	def run_validators(self, value):
		for validator in self.validators:
			if isinstance(validator, validators.UniqueTogetherValidator):
				self.validators.remove(validator)
		super(ProviderSerializer, self).run_validators(value)

	def create(self, validated_data):
		user = validated_data.pop('user')
		provider,_ = Provider.objects.get_or_create(user=user, **validated_data)
		return provider


	def update(self, instance, validated_data):
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.last_name = validated_data.get('last_name', instance.last_name)
		instance.address = validated_data.get('address', instance.address)
		instance.rate = validated_data.get('rate', instance.rate)
		instance.gender = validated_data.get('gender', instance.gender)
		services = validated_data.pop('services')
		instance.save()
		return instance

	def to_representation(self, *arrgs, **kwargs):
		self.fields['services']= ServiceSerializer(context=self.context, many=True)
		return super().to_representation(*arrgs, **kwargs)



# class ProviderServiceSerializer(serializers.Serializer):
# 	services = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True, required=False)

# 	def run_validators(self, value):
# 		for validator in self.validators:
# 			if isinstance(validator, validators.UniqueTogetherValidator):
# 				self.validators.remove(validator)
# 		super(ProviderSerializer, self).run_validators(value)

# 	def create(self, validated_data):
# 		user = validated_data.pop('user')
# 		user = validated_data.pop('services')
# 		provider,_ = Provider.objects.get_or_create(user=user, **validated_data)
# 		return provider
