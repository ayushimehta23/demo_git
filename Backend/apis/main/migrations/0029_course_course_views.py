# Generated by Django 4.2 on 2023-05-25 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_studymaterial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_views',
            field=models.IntegerField(default=0),
        ),
    ]