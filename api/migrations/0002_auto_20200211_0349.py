# Generated by Django 3.0.3 on 2020-02-11 02:49

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_body',
            field=tinymce.models.HTMLField(),
        ),
    ]