from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=100)
    describe = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.pk])


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'normal'),
        ('4', 'good'),
        ('5', 'perfect'),
    ]

    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("product_detail", args = [self.product.id])
    
    
    
