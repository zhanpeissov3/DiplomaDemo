from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Service(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    icon = models.ImageField(upload_to='icons/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.TextField()
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Meta:
    ordering = ('title',)
    verbose_name = 'Услуга'
    verbose_name_plural = 'Услуги'


def __str__(self):
    return self.title
