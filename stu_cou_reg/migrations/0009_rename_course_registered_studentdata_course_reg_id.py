# Generated by Django 4.2.1 on 2023-05-25 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stu_cou_reg', '0008_alter_studentdata_course_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentdata',
            old_name='course_registered',
            new_name='course_reg_id',
        ),
    ]
