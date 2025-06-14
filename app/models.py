from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount, HitCountMixin



class Categories(models.Model):
    name=models.CharField(max_length=50)
    
    def str(self):
        return self.name
 
class BlogCategories(models.Model):
    name = models.CharField(max_length=150)
    def str(self):
        return self.name
    
class Blog(models.Model ,HitCountMixin):
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=170)
    description=RichTextField()
    created_data=models.DateTimeField(auto_now_add=True)
    categories=models.ForeignKey(BlogCategories, on_delete=models.CASCADE)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    created_data = models.DateTimeField(auto_now_add=True)
    def str(self):
        return f"{self.title}"
    

    
class Contact(models.Model):
    firstname = models.CharField(max_length=70)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def str(self):
        return f"{self.firstname} {self.lastname}  {self.email} {self.subject} {self.message}"