# Generated by Django 3.2.13 on 2023-01-30 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_posts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]