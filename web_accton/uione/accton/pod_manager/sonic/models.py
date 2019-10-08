from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE,verbose_name='留言者id')
    title = models.CharField(max_length=255,null=True, verbose_name='文章標題')
    content = models.TextField(null=True, verbose_name='文章內容')
    awesome_number = models.IntegerField(null=True, verbose_name='按贊數量')
    time = models.DateTimeField(auto_now_add=True,null=True, verbose_name='创建时间')
    view_number = models.IntegerField(null=True, verbose_name='瀏覽量')

class Ｍessage(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE,verbose_name='留言者id')
    article = models.ForeignKey(Article,null=True, on_delete=models.CASCADE, verbose_name='留言的文章id')
    main_message = models.ForeignKey("self",null=True, on_delete=models.CASCADE, verbose_name='回復的留言id')
    content = models.TextField(null=True, verbose_name='留言內容')
    awesome_number = models.IntegerField(null=True, verbose_name='按贊數量')
    bad_number = models.IntegerField(null=True, verbose_name='按爛數量')
    time = models.DateTimeField(auto_now=True,null=True, verbose_name='创建时间')

class User_Type(models.Model):
    user =  models.ForeignKey(User,null=True, on_delete=models.CASCADE,verbose_name='留言者id')
    user_type_id = models.IntegerField(null=False,verbose_name='type id')

class Article_Tag(models.Model):
    tag_name = models.CharField(max_length=30,null=True)
    article = models.ForeignKey(Article,null=True, on_delete=models.CASCADE,related_name = "tag")

class Message_User(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE,verbose_name='按贊者id')
    message = models.ForeignKey(Message,null=True,on_delete=models.CASCADE,verbose_name='訊息')
    article = models.ForeignKey(Article,null=True, on_delete=models.CASCADE, verbose_name='留言的文章id')
    judge_type = models.CharField(max_length=12,null=True, verbose_name='按贊')
