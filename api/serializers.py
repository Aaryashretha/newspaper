from django.contrib.auth.models import Group, User
from newspaper.models import Category, Post, Tag
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email','first_name','last_name', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields=[
            "id",
            "title",
            "content",
            "featured_image",
            "status",
            "tag",
            "category",
            "author",
            "views_count",
            "published_at",
        ]
        extra_kwargs ={
            "author": {"read_only": True},
            "views_count":{"read_only":True},
            "published_at":{"read_only": True},
        }

    def validate(self, data):
            data["author"] = self.context["request"].user
            return data

