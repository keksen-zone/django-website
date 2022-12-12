from django.db import models

# Create your models here.

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.TextField()
    author = models.TextField(null=True)
    abstract = models.TextField(null=True)
    publish_date = models.DateTimeField(auto_now=True)
    big_class = models.TextField(null=True)
    small_class = models.TextField(null=True)

    def __str__(self):
        return self.title
