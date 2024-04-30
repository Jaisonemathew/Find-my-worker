from django.db import models
# Create your models here.

class Worker(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to="pics")
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
    is_approved = models.BooleanField(default=False)

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



