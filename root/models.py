from django.db import models
from django.contrib.auth.models import User



class Testimonials(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials', default='default.JPEG')
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Pros(models.Model):
    title = models.TextField()
    status = models.BooleanField()

    def __str__(self):
        return self.title

class Prices(models.Model):
    title = models.TextField() 
    price = models.IntegerField()
    pros = models.ManyToManyField(Pros)
    status = models.BooleanField()

    def __str__(self):
        return self.title

class Services(models.Model):
    title = models.TextField()
    desc = models.TextField()
    status = models.BooleanField()

    def __str__(self):
        return self.title

class Services_two(models.Model):
    title = models.TextField()
    desc = models.TextField()
    status = models.BooleanField()

    def __str__(self):
        return self.title

class FQA(models.Model):
    title = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.title

