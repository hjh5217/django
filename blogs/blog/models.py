import os

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    photo = models.ImageField(upload_to='blog/images/%Y/%m/%d/',
                              null=True,blank=True)
    file = models.FileField(upload_to='blog/files/%Y/%m/%d/',
                            null=True,blank=True)
    def __str__(self):
        return self.title

    # 파일의 이름 출력
    def get_file_name(self):
        return os.path.basename(self.file.name)
