# Generated by Django 2.2 on 2019-06-13 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sonic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_tag',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='sonic.Article'),
        ),
    ]
