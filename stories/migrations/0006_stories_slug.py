# Generated by Django 4.0.3 on 2022-04-06 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_rename_story_stories'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
