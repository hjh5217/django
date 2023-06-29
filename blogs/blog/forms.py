from django import forms

from blog.models import Post

# 포스트 폼 생성
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'file']
        labels = {
            'title': '제목',
            'content': '냉용',
            'photo': '사진',
            'file': '파일',
        }