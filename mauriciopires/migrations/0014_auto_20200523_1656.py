# Generated by Django 3.0.6 on 2020-05-23 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mauriciopires', '0013_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographers',
            name='type_user',
            field=models.CharField(choices=[('Admin', 'Admin'), ('User', 'User')], max_length=50),
        ),
    ]
