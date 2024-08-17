from django.db import models
from django.core.exceptions import ValidationError
#Email
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

class Customer(models.Model):
    customer=models.OneToOneField(User,on_delete=models.CASCADE)
    is_customer=models.BooleanField(default=True)
    name=models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.name

class Worker(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to="pics",blank=True,null=True)
    worker=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    is_customer=models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class booking(models.Model):
    user=models.CharField(max_length=20)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    phno=models.CharField(max_length=10)
    address=models.TextField()
    district=models.CharField(max_length=25)
    amount=models.TextField()
    worker=models.CharField(max_length=25)
    email = models.CharField(max_length=254,default='')
    is_approved = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if self.is_approved and self.is_cancelled:
            raise ValidationError("A booking cannot be both approved and cancelled.")
        super().save(*args, **kwargs)
    
    
#Email System
@receiver(post_save, sender=booking)
def send_notification(sender, instance, created, **kwargs):
    if not created and instance.is_approved:
        try:
            message = 'Dear {},\n\nYour booking has been approved.\n\nDetails:\nPhone Number: {}\nEmail: {}\nAddress: {}\nDistrict: {}\nNo of Worker: {}\nWorker: {}'.format(
                instance.firstname,
                instance.phno,
                instance.email,
                instance.address,
                instance.district,
                instance.amount,
                instance.worker
            )
            send_mail(
                'Your booking has been approved',
                message,
                settings.EMAIL_HOST_USER,
                [instance.email],
                fail_silently=False,
            )
        except Exception as e:
            # Log the exception or handle it as needed
            print(f"Failed to send email: {e}")

    def __str__(self):
        return self.user




class feedback(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    message=models.TextField()
    

    def __str__(self):
        return self.email

class notification(models.Model):

    email=models.CharField(max_length=200)
    

    def __str__(self):
        return self.email

class review(models.Model):

    name=models.CharField(max_length=20)
    email=models.CharField(max_length=200)
    message=models.TextField()
    

    def __str__(self):
        return self.name



