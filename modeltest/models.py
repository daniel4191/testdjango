from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("제목",max_length=30)
    content = models.TextField("내용")
    
    def __str__(self):
        return f"{self.title}: {self.content}"
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="선택할 포스트")
    comment = models.TextField("댓글내용")
    
    def __str__(self):
        return f"선택한 포스트:{self.post} / 댓글내용: {self.comment}"