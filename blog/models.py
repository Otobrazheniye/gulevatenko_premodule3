from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    subscribers = models.ManyToManyField(User,related_name="subscribed_topics", blank = True)  

    def __str__(self):
        return f"{self.name}"


class Article(models.Model):
    author = models.ForeignKey(User,related_name="articles",on_delete=models.CASCADE)
    topics = models.ManyToManyField(Topic,related_name="articles",blank = False)

    title = models.CharField(max_length=200)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    

class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User,related_name="comments",on_delete=models.CASCADE)
    article = models.ForeignKey(Article,related_name="comments",on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.author} \n\t{self.text}"
