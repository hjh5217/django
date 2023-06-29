from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    # 제목, 내용, 등록일
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    # 내용, 작성일
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.content