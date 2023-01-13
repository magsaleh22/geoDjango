from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import *


class MunicipilitiesLocationSerializer(GeoFeatureModelSerializer):
    """a class to serialize locations as GeoJSON compatible data"""
    class Meta:
        model = Municipalities
        geo_field = "location"
        fields = '__all__'
        
        
class MunicipilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipalities
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email']
        extra_kwargs = {
            'password': {'write_only':True}
        }
        
    def create(self,validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return {
            "username" : user.username,
            "email" : user.email
        }
        