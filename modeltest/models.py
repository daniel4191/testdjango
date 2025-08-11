from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("제목",max_length=30)
    content = models.TextField("내용")
    
    def __str__(self):
        return f"{self.title}: {self.content}"