# Generated by Django 2.2 on 2019-06-11 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='文章標題')),
                ('content', models.TextField(null=True, verbose_name='文章內容')),
                ('awesome_number', models.IntegerField(null=True, verbose_name='按贊數量')),
                ('time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('view_number', models.IntegerField(null=True, verbose_name='瀏覽量')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='留言者id')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True, verbose_name='留言內容')),
                ('awesome_number', models.IntegerField(null=True, verbose_name='按贊數量')),
                ('bad_number', models.IntegerField(null=True, verbose_name='按爛數量')),
                ('time', models.DateTimeField(auto_now=True, null=True, verbose_name='创建时间')),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sonic.Article', verbose_name='留言的文章id')),
                ('main_message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sonic.Message', verbose_name='回復的留言id')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='留言者id')),
            ],
        ),
        migrations.CreateModel(
            name='User_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type_id', models.IntegerField(verbose_name='type id')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='留言者id')),
            ],
        ),
        migrations.CreateModel(
            name='Message_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judge_type', models.CharField(max_length=12, null=True, verbose_name='按贊')),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sonic.Article', verbose_name='留言的文章id')),
                ('message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sonic.Message', verbose_name='訊息')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='按贊者id')),
            ],
        ),
        migrations.CreateModel(
            name='Article_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30, null=True)),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sonic.Article')),
            ],
        ),
    ]
