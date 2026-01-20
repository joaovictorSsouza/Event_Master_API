from rest_framework import serializers
from .models import Event, Categories
from django.contrib.auth.models import User

class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):

    category_details = CategoriesSerializer(source='category', read_only=True)
    owner_name = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Event
        fields = ['id',
                  'event_name',
                  'description',
                  'date',
                  'location',
                  'is_remote',
                  'capacity',
                  'price',
                  'category',
                  'category_details',
                  'owner',
                  'owner_name',]
        
        read_only_fields = ['owner']


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
     
