# Generated by Django 4.2 on 2023-06-01 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_teacherstudentchat'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='facebook_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='instagram_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='twitter_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='website_url',
            field=models.URLField(null=True),
        ),
    ]
