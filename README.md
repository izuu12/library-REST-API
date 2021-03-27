# library-REST-API

##Description

An application that has a simple REST-API in the Django framework.
##Installation
* Open your project folder.
* Create a virtual environment
* install Django and fdjangorestframework
* Add this project
* Install postgreSQL db on your computer and PgAdmin

##Usage
if you want to use the app on lokalhost, uncomment DATABASES = {...} and comment
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES = {'default': dj_database_url.config('DATABASE_URL',default='postgres://localhost')}

-SORT
  if you want to sort by the published_date field in the search engine, paste:
          http://127.0.0.1:8000/api/books/?ordering=published_date
      result -> list of books in the database sorted from oldest to youngest JASON
          http://127.0.0.1:8000/api/books/?ordering=-published_date
      result ->list of books in the database sorted from youngest to oldest JSON
-GET BOOK by id
  if you want to take a book with a specific id
           http://127.0.0.1:8000/api/books/40/
        result -> a book with a specific id JASON
- GET authors
  if you want to take books from specific authors
           http://127.0.0.1:8000/api/books/?authors=<authors>&authors=<authors>
           np: http://127.0.0.1:8000/api/books/?authors=kotarski&authors=J.%20R.%20R.%20Tolkien
           result -> list of books by the authors mentioned JASON
-POST {}
if you want to add a book by sending data about it in JSON format
            in postman use POST method, enter request url: http://127.0.0.1:8000/api/books/
            choose body, raw add JSON np.:
                    {
                        "title": "Hobbit czyli Tam i z powrotem",
                        "authors": [
                          "J. R. R. Tolkien"
                        ],
                        "published_date": "2004",
                        "categories": [
                          "Baggins, Bilbo (Fictitious character)"
                        ],
                        "average_rating": 5,
                        "ratings_count": 3,
                        "thumbnail": "http://books.google.com/books/content?id=YyXoAAAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
                    }
           title, published_date and thumbnail fields are required
           result -> added book JASON
-DOWNLOAD date set from url - POST
      If you want to add multiple books from JSON using url
                   in postman use POST method, enter request url: http://127.0.0.1:8000/api/books/updateDataSet/

                   choos form-data and add kay: 'url' value url path np: https://www.googleapis.com/books/v1/volumes?q=war
                   result->list of books from url JASON
                   result-> if the specified books already exist in the database : "the related books already exist in the database"
