from rest_framework import serializers
# import models
# # data = serializers.serialize("xml", models.customer_details.objects.all(), fields=["name", "size"])
# data = serializers.serialize("xml", models.customer_details.objects.all())
# print(data)
from .models import CustomerDetails
# class UserSerializer(serializers.Serializer):
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     phone_number = serializers.IntegerField()
#     customer_id = serializers.IntegerField()
#     order_id = serializers.IntegerField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetails
        fields = '__all__'  # Adjust fields as necessary

    def update(self, instance, validated_data):
        # Iterate over the validated data and update each field
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()  # Save the updated instance
        return instance