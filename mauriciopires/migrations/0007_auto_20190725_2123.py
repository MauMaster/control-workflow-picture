# Generated by Django 2.1.7 on 2019-07-26 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mauriciopires', '0006_auto_20190725_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='checkin',
            field=models.DateField(max_length=50),
        ),
        migrations.AlterField(
            model_name='images',
            name='checkout',
            field=models.DateField(blank=True, max_length=50, null=True),
        ),
    ]
