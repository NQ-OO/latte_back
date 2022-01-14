from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from latte.models import School
# Create your models here.


# class Profile(models.Model):
#     GENDER_CHOICES = [
#       ('M', 'Male'),
#       ('F', 'Female'),
#       ('N', 'I Prefer Not To Say'),
#     ]   

#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=20, blank=True)    
#     nickname = models.CharField(max_length=20, blank=True)
#     # password = models.CharField(max_length = 200)
#     school = models.ForeignKey(School, on_delete=models.CASCADE, null=False, default=1)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)    
#     major = models.CharField(max_length=20, blank=True)
#     # created_at = models.DateTimeField(default=timezone.now)
#     # updated_at = models.DateTimeField(blank=True, null=True)

#     def __str__(self):   # 추가        
#         return f'id={self.id}, user_id={self.user.id}, nickname={self.nickname}, school={self.school}, gender={self.gender}, major={self.major}'

#     @receiver(post_save, sender=User)  
#     def create_user_profile(sender, instance, created, **kwargs):        
#         if created:          
#             Profile.objects.create(user=instance)  
    
#     @receiver(post_save, sender=User)  
#     def save_user_profile(sender, instance, **kwargs):        
#         instance.profile.save()
