# Generated by Django 2.1.7 on 2019-10-05 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mauriciopires', '0010_auto_20191005_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='number',
            field=models.IntegerField(),
        ),
    ]
