# Generated by Django 4.1.5 on 2023-02-10 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0017_comments_comments_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]