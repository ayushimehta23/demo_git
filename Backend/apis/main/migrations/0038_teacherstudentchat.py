# Generated by Django 4.2 on 2023-05-31 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_remove_student_login_via_otp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherStudentChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_txt', models.TextField()),
                ('msg_from', models.CharField(max_length=100)),
                ('msg_time', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teacher')),
            ],
            options={
                'verbose_name_plural': '18. Teacher Student Messages',
            },
        ),
    ]
