from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	portfolio_site = models.URLField(blank=True)
	profile_pict = models.ImageField(upload_to='profile_pics',blank=True)
	def __str__(self):
  		return self.user.username
# Create your models here.
class Post(models.Model):
	user_name=models.CharField(max_length=200,null=False)
	post_title=models.CharField(max_length=200,null=False)
	post_content=models.TextField(default='tutorial content')
	date_published=models.DateField(blank=True,null=True)
	user_profile_link=models.URLField(blank=True,null=True)
	def __str__(self):
  		return self.user_name
