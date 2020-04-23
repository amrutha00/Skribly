# Generated by Django 3.0.4 on 2020-04-23 11:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Skribbly', '0004_auto_20200421_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comicstrip',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='downvotes',
            field=models.ManyToManyField(blank=True, related_name='downvotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
