from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=120)


    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',null=True, blank=True)
    name = models.CharField(max_length=90)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=30)
