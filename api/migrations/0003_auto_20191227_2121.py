# Generated by Django 3.0 on 2019-12-27 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191227_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='author',
            new_name='owner',
        ),
    ]