from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    subscribers = models.ManyToManyField(User,related_name="subscribed_topics", blank = True)  

    def __str__(self):
        return f"{self.name}"

# SQL
# CREATE TABLE blog_topic (
#     id BIGSERIAL PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     created_at TIMESTAMP WITH TIME ZONE NOT NULL
# );


class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="articles")
    topics = models.ManyToManyField(Topic,related_name="articles")

    title = models.CharField(max_length=200)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    

class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name="comments")

    def __str__(self):
        return f"Comment by {self.author} on {self.article}"

