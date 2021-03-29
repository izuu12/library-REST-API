from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.core.exceptions import ValidationError
import re
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    """
    Book - class create the essential fields and behaviors of the data
    """
    title = models.CharField(max_length=300, blank=False, null=True)
    authors =ArrayField(models.CharField(max_length=100), default=list,null=True,blank=True)
    published_date= models.CharField(default =2000,blank=False, max_length=10)
    categories = ArrayField(models.TextField(),null=True,blank=True,default=list)
    #average_rating = models.DecimalField(max_digits=2, decimal_places=1,blank=True, null=True)
    average_rating = models.FloatField(max_length=3,blank=True, null=True,validators=[MinValueValidator(0),MaxValueValidator(6)])
    ratings_count=models.IntegerField(blank=True, null=True,validators=[MinValueValidator(0)])
    thumbnail =models.URLField(max_length=300,unique=False, null=True, blank=False)
    def clean(self):
        """
        clean -validates the format of the value entered in the published_date field and rounds the number of decimal
               places to two for the average_rating field
        """
        if self.published_date!=None:
            if len(self.published_date) ==4:
                x = re.search(r"^(\d{4})$", self.published_date)
                if x == None:
                    raise ValidationError('field Published date accepts date format : YYYY-MM-DD or YYYY')
                else:
                    print("No match")
            elif len(self.published_date) == 10:
                x = re.search(r"^(\d{4}\-)([0-1]{1}\d{1}\-)([0-3]{1}\d{1})$", self.published_date)
                if x ==None:
                    raise ValidationError('field Published date accepts date format : YYYY-MM-DD or YYYY')
            else:
                raise ValidationError('field Published date accepts date format : YYYY-MM-DD or YYYY')
        if self.average_rating!=None:
            try:
                return round(float(self.average_rating), 2)
            except:
                raise ValidationError('valus {}  is not an integer or a float  number'.format(self.average_rating))

class Item(models.Model):
    """
    Items - class create the essential fields and behaviors of the data
    """
    kind = models.CharField(default="books#volume",max_length=30)
    book = models.ManyToManyField(Book, related_name='book')










