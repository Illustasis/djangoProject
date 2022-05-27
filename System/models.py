from django.db import models


class User(models.Model):
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    user_id = models.AutoField(primary_key=True)


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    image = models.CharField(max_length=200)  # 封面图片
    author = models.CharField(max_length=80)
    press = models.CharField(max_length=80)  # 出版社
    introduction = models.TextField(max_length=1000, default='')
    score = models.DecimalField(max_digits=1, decimal_places=1)  # 评分，5分满分，1位小数
    heat = models.IntegerField(default=0)  # 点击量


class Score(models.Model):  # 评分表
    user_id = models.IntegerField(default=0)
    resource_id = models.IntegerField(default=0)   # 相关资源（book,movie)的id
    score = models.IntegerField(default=0)


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    text = models.TextField(max_length=1000, default='')
    author_id = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    heat = models.IntegerField(default=0)
    column = models.IntegerField(default=0)  # 分类 1:book,2:movie,3:topic
    resource_id = models.IntegerField(default=0)  # 相关资源（book,movie,topic）的id
    likes = models.IntegerField(default=0)


class Collect(models.Model):
    user_id = models.IntegerField(default=0)
    resource_id = models.IntegerField(default=0)  # 相关资源（book,movie,topic，group）的id
    column = models.IntegerField(default=0)  # 分类 1:book,2:movie,3:topic,4:group


class Reply(models.Model):
    reply_id = models.AutoField(primary_key=True)
    article_id = models.IntegerField(default=0)
    text = models.CharField(max_length=80)
    likes = models.IntegerField(default=0)
    author_id = models.IntegerField(default=0)
    reply_to = models.IntegerField(default=0)
