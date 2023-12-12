from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
class UserModel(models.Model):
    class Meta:
        db_table = "my_user"
    
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)

class Post(models.Model):
    models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='intruder_image/%Y/%m/%d/')
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
