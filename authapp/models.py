from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=13)
    content=models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
    
    # ye admin panel me jb koi contact form fill krta h to bahar se use kaise show krna h uska structure h 
    def __str__(self):
        return 'Message from ' + self.name + ' ' +  self.email