# Generated by Django 4.1.5 on 2023-02-03 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0013_rename_post_id_likes_post_rename_user_id_likes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=22),
        ),
    ]
