# Generated by Django 2.1.7 on 2019-08-04 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mauriciopires', '0008_auto_20190804_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographers',
            name='type_user',
            field=models.CharField(choices=[('Admin', 'Administrator'), ('User', 'User')], default='User', max_length=50),
        ),
    ]
