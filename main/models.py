from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class Profile(AbstractUser):
    profile_picture = models.ImageField()
    bio = models.TextField('Bio',null =True)
    birth_date = models.DateField('Birth Date',null=True)

    def __str__(self):
        return self.username 

class Hobby(models.Model):
    interest_text = models.CharField(max_length=200)
    interest_desc = models.TextField('Description')

    def __str__(self):
        return self.interest_text

#Used for defining when an user is interested in particular hobies
class HobbyInterest(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    hobby = models.ForeignKey(Hobby,on_delete=models.CASCADE)
    interest_reason = models.CharField(max_length=400,verbose_name='Why the Interest')
    interest_date = models.DateField('Interested Since')

    def __str__(self):
        return self.profile.username + " likes " + self.hobby.interest_text

    



