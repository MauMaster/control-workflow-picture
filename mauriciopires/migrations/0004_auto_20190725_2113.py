# Generated by Django 2.1.7 on 2019-07-26 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mauriciopires', '0003_auto_20190725_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='name',
            field=models.CharField(max_length=19),
        ),
    ]
