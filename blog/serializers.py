from django.contrib.auth.models import User
from rest_framework import serializers, fields
from rest_framework.fields import SerializerMethodField

from blog.models import Blog, Comment


class UserRegisterSerializer(serializers.ModelSerializer):
    pass


class UserLoginSerializer(serializers.ModelSerializer):
    pass


class UserSerializer(serializers.ModelSerializer):
    pass


class BlogListSerializer(serializers.ModelSerializer):

    pass


class BlogDetailSerializer(serializers.ModelSerializer):

    pass


class BlogPostSerializer(serializers.ModelSerializer):

    pass


class CommentListSerializer(serializers.ModelSerializer):

    pass


class CommentSerializer(serializers.ModelSerializer):

    pass


