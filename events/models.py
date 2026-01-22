from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):

    id = models.AutoField(primary_key=True)
    categories = models.CharField(max_length=200)

    def __str__(self):
        return self.categories

class Event(models.Model):

    id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=200)
    #Colocar depois o help_text= para explicar
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=200, null=True, blank=True)
    is_remote = models.BooleanField(default=False)
    capacity = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='category_list', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_user')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name
    