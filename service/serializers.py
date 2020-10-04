from rest_framework import serializers
from .models import Category, ServiceType, Service
from collections import defaultdict
from provider.models import Provider



class ServiceTypeSerializer(serializers.Serializer):
	id=serializers.ReadOnlyField()
	service_type = serializers.CharField(max_length=500)


	def run_validators(self, value):
		for validator in self.validators:
			if isinstance(validator, validators.UniqueTogetherValidator):
				self.validators.remove(validator)
		super(ServiceTypeSerializer, self).run_validators(value)

	def create(self, validated_data):
		category,_ = ServiceType.objects.get_or_create(**validated_data)
		return category


	def update(self, instance, validated_data):
		instance.service_type = validated_data.get('service_type', instance.service_type)
		instance.save()
		return instance


class CategorySerializer(serializers.Serializer):
	id=serializers.ReadOnlyField()
	name = serializers.CharField(max_length=200)
	service_types = serializers.PrimaryKeyRelatedField(queryset=ServiceType.objects.all(), many=True)


	def run_validators(self, value):
		for validator in self.validators:
			if isinstance(validator, validators.UniqueTogetherValidator):
				self.validators.remove(validator)
		super(CategorySerializer, self).run_validators(value)

	def create(self, validated_data):
		service_types = validated_data.pop('service_types')
		name = validated_data.pop('name')
		category,_ = Category.objects.get_or_create(name=name, **validated_data)
		category.service_types.set(service_types)
		return category

		
	def update(self, instance, validated_data):
		service_types = validated_data.pop('service_types')
		instance.name = validated_data.get('name', instance.name)
		instance.service_types.set(service_types)
		instance.save()
		return instance


	# def to_representation(self, *arrgs, **kwargs):
	# 	self.fields['category']= CategorySerializer(context=self.context, many=False)
	# 	return super().to_representation(*arrgs, **kwargs)





class ServiceSerializer(serializers.Serializer):
	id=serializers.ReadOnlyField()
	category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False, many=False)
	service_type = serializers.PrimaryKeyRelatedField(queryset=ServiceType.objects.all(), many=False, required=False)


	def run_validators(self, value):
		for validator in self.validators:
			if isinstance(validator, validators.UniqueTogetherValidator):
				self.validators.remove(validator)
		super(ServiceSerializer, self).run_validators(value)

	def create(self, validated_data):
		category = validated_data.pop('category')
		service_type = validated_data.pop('service_type')
		service, _= Service.objects.get_or_create(category=category, service_type=service_type)
		return service

	# def validate(self, attrs):
	# 	errors =defaultdict(list)
	# 	category = attrs['category']
	# 	service_type = attrs['service_type']
	# 	service_type = ServiceType.objects.filter(service_type=service_type).first()
	# 	if not self.instance and category:
	# 		errors['category'].append('Already registered.')
	# 	if errors:
	# 		raise serializers.ValidationError(errors)

	# 	return attrs

	def update(self, instance, validated_data):
		instance.category = validated_data.get('category', instance.category)
		instance.service_type = validated_data.get('service_type', instance.service_type)
		instance.save()
		return instance









