# Generated by Django 4.1 on 2022-08-18 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0003_alter_user_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(verbose_name='%m-%d-%y'),
        ),
    ]
