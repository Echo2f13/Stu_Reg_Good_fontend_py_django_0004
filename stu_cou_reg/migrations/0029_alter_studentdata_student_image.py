# Generated by Django 4.2.1 on 2023-05-30 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu_cou_reg', '0028_alter_regisatered_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='student_image',
            field=models.ImageField(null='True', upload_to=''),
        ),
    ]