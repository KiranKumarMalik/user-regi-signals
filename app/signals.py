from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User
from django.core.mail import send_mail
from app.models import Profile
import os
@receiver(post_save,sender=User)
def send_mail_for_user(sender,instance,created,**kwargs):
    if created:
        email=instance.email
        send_mail('Registration',
                  'Successfull',
                  'harshadvali09@gmail.com',
                  [email],
                  fail_silently=False
                  )

@receiver(post_delete,sender=Profile)
def delete_profile_pic(sender,instance,**kwargs):
    if instance.profile_pic:
        filepath=instance.profile_pic.path
        if os.path.isfile(filepath):
            os.remove(filepath)







    