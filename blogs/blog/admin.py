from django.contrib import admin
from .models import Post

# Register your models here.
# 관리자 페이지에 post 등록

admin.site.register(Post)