# Generated by Django 4.2.1 on 2023-06-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu_cou_reg', '0034_alter_registereddata_date_apply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registereddata',
            name='date_approve',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
