# Generated by Django 5.2.3 on 2025-06-30 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Blog_Post',
        ),
    ]
