# Generated by Django 4.2 on 2023-05-18 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_notification_alter_student_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name_plural': '10. Notification'},
        ),
        migrations.RemoveField(
            model_name='notification',
            name='notif_text',
        ),
        migrations.AlterField(
            model_name='notification',
            name='notif_for',
            field=models.CharField(max_length=200, verbose_name='Notification For'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notifread_status',
            field=models.BooleanField(default=False, verbose_name='Notification Status'),
        ),
    ]
