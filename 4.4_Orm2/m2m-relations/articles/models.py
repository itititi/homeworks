from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=100)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default='default_value')
    sections = models.ManyToManyField(Section, through='ArticleSection')

    def __str__(self):
        return self.title


class ArticleSection(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)
