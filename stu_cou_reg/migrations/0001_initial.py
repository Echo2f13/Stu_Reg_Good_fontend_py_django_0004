# Generated by Django 4.2.1 on 2023-05-25 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseData',
            fields=[
                ('course_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=16, null=True, unique=True)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('student_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('course_status', models.BooleanField(default=False)),
                ('student_image', models.ImageField(upload_to='')),
                ('course_registered', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stu_cou_reg.coursedata')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]
