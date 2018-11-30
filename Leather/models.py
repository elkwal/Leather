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
    category = models.ForeignKey(Category, related_name='products',null=True, blank=True, on_delete=models.CASCADE)
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

class Town(models.Model):
    name = models.CharField(max_length=20, unique=True)
    bio = models.CharField(max_length=40, default='')
    admin = models.ForeignKey(User_profile, related_name='administrate',on_delete=models.CASCADE)

    def save_town(self):
        self.save()

    def remove_town(self):
        self.delete()

    @classmethod
    def get_town(cls, id):
        town = Town.objects.get(id=id)
        return town


class Profile(models.Model):
    user = models.OneToOneField(User_profile, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=25, unique=True)
    bio = models.TextField(max_length=100, blank=True)
    profilepic = models.ImageField(upload_to='picture/', default=True)
    email = models.EmailField()
    contact = models.CharField(max_length=15, blank=True)
    townpin = models.BooleanField(default=False)
    town = models.ForeignKey(Town, related_name='home', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    @classmethod
    def search_by_username(cls, search_query):
        profiles = cls.objects.filter(user__username__icontains=search_query)
        return profiles

    @classmethod
    def updateimage(cls, id):
        image = cls.objects.get(id=id)
        return image


class Post(models.Model):
    title = models.CharField(max_length=30)
    post = models.TextField(max_length=100)
    hood = models.ForeignKey(Town, related_name='town', on_delete=models.CASCADE)
    poster = models.ForeignKey(User_profile, on_delete=models.CASCADE)
    postpic = models.ImageField(upload_to='picture/', default=True)

    def save_post(self):
        self.save()

    def remove_post(self):
        self.delete()

    @classmethod
    def get_town_posts(cls, id):
        posts = Post.objects.filter(id=id)
        return posts

    @classmethod
    def post_comments(cls, id):
        comments = cls.objects.filter(postcomments__comment_id=id)
        posters = cls.objects.filter(postcomments__commnetator__id=id)
        return comments, posters


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    commentator = models.ForeignKey(User_profile,on_delete=models.CASCADE)
    comment_post = models.ForeignKey(Post, related_name='comment', null=True,on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()


