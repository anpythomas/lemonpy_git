# Generated by Django 4.1.5 on 2023-01-26 13:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_alter_post_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.FloatField(max_length=20, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]