from rest_framework import serializers
from django.contrib.auth import get_user_model 
from posts.models import Post
from children.models import Children


class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = ('registrar', 'clinic', 'ward','card_number','certificate_number','firs_name','mother_name','father_name','address','gender','date_of_birth',)
        

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'user', 'body', 'date')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = ('id', 'username',)
