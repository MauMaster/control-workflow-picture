# Generated by Django 2.1.7 on 2019-10-05 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mauriciopires', '0009_photographers_type_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='number',
            field=models.IntegerField(max_length=19),
        ),
    ]
