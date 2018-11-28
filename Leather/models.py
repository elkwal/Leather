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



class Business(models.Model):
    Bizname=models.CharField(max_length=60)
    profile=models.ForeignKey(Product,on_delete=models.CASCADE)
    biz_email=models.EmailField()
    biz_desc=models.CharField(max_length=100)

    @classmethod
    def search_biz(cls,search_term):
        
        business=cls.objects.filter(Bizname__icontains=search_term)
        return business


    @classmethod
    def create_business():
        pass

    @classmethod
    def delete_business():
        pass

    @classmethod
    def find_business(business_id):
        pass

    @classmethod
    def update_business():
        pass



class User_profile(models.Model):
    name=models.CharField(max_length=60)
    product=models.ForeignKey(Product,null=True,on_delete=models.CASCADE)
    email=models.EmailField()
    profile_photo=models.ImageField(upload_to='gallery/',blank=True,null=True)


    @classmethod
    def get_profile(cls): 
        profile=profile_photo.objects.all()
        return profile



