from django.contrib.auth.models import User
from .models import Book, Item
from rest_framework import serializers
from django.http import HttpResponse


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class BooksSerializer(serializers.ModelSerializer):
    """
    BooksSerializer - serializes data from the Books class to JASON
    """
    class Meta:
        model = Book

        fields = ['title', 'authors','published_date','categories', 'average_rating','ratings_count','thumbnail']

    def create(self, validated_data):
        """
        create - the method returns Book class objects created from values sent with the post method
        :param validated_data - dict
        :return returns a Book object that was created serialized to the JASON front
        """
        book,create=Book.objects.update_or_create(**validated_data)
        return book




class ItemSerializer(serializers.ModelSerializer):
    """
        BooksSerializer - serializes data from the Item class to JASON
    """
    class Meta:
        model = Item
        fields = ['kind','book']



