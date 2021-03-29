import urllib.request, json
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import (UserSerializer, BooksSerializer, ItemSerializer)
from .models import (Book,Item)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    """
    BookViewSet -class allows you to create queries and returns an object or objects of the class Books
    """
    serializer_class = BooksSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    #filterset_fields = ['published_date']
    ordering_fields = ['published_date']

    def get_queryset(self):
        """
        get_queryset - the method allows you to return an object or objects of the Book class serialized to JSON
         from the database after applying a filter
        :return return an object or objects of the book class serialized to JSON

        """
        authors = self.request.query_params.getlist("authors")
        data = self.request.query_params.get("published_date")
        books = Book.objects.all()
        if authors:
            books = books.filter(authors__overlap = authors)
        if data:
            books =books.filter(published_date__startswith=data)
        return books

    # use api/books/updateDataSet/
    # in the POST method, enter the key "url" and as value the url that will contain the JASON file
    @action(detail=False, methods=['post'])
    def updateDataSet(self,request, **kwargs):
        """
        updateDataSet - the method returns the serialized object or objects of the Book class to type JASON,
                        which were created  or update from the url containing JASON

        :param request - dictionary, contains sent values​by POST method
        :return an object or objects of the book class serialized to JSON, or HttpResponse(text) where text is a message
        """
        try:
            #read JASON
            url_dataBase = request.data['url']
            with urllib.request.urlopen(url_dataBase) as url:
                json_data = json.loads(url.read().decode())
                #creating an object of class Item
                item_create = Item.objects.create()
                item_create.save()
                add = 0
                #create an object of the class Book and add it to the object of class Item in each iteration
                for item in json_data['items']:
                    #if the book does not exist in the database, add it. if exist update
                    # check if the key is in the dictionary if so write the dictionary value to the names list
                    names = ['categories', 'authors', 'averageRating', 'ratingsCount', 'publishedDate']
                    value = [[], [], None, None, None]
                    for nr, name in enumerate(names):
                        if name in item['volumeInfo'].keys():
                            value[nr] = item['volumeInfo'][name]
                    #create book
                    book,created = Book.objects.update_or_create(
                        title=item['volumeInfo']['title'], authors=value[1],
                        published_date=value[4],categories=value[0],average_rating = value[2],ratings_count = value[3],
                        thumbnail=item['volumeInfo']['imageLinks']['thumbnail'])
                    print(book,created)
                    book.save()
                    #add book to item
                    item_create.book.add(book)
                    if created==True:
                        add+=1
        except :
            text = "can't create database"
            return HttpResponse(text)
        else:
            if add==0:
                item_create.delete()
                text = "update database"
                return HttpResponse(text)
            else:
                item_create.save()
                serializer = ItemSerializer(item_create, many=False)
                return Response(serializer.data)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer







