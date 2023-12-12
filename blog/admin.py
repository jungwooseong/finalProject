from django.contrib import admin
from .models import UserModel
from .models import Post
# Register your models here.
admin.site.register(UserModel)
admin.site.register(Post)