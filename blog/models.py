from django.conf import settings
from django.db import models
from django.utils import timezone


"""models.Model はポストがDjango Modelだという意味"""
class Post(models.Model):
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    """文字数が制限されたテキストを定義するフィールド"""
    title = models.CharField(max_length=200)
    """これは制限無しの長いテキスト用"""
    text = models.TextField()
    
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
"""第1引数はselfにするルール"""
    def publish(self):
        """published_dateにtimezone.now()を渡す"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title