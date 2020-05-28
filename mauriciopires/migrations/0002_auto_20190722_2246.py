# Generated by Django 2.1.7 on 2019-07-23 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mauriciopires', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='user',
        ),
        migrations.AddField(
            model_name='images',
            name='name',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='mauriciopires.Photographers'),
            preserve_default=False,
        ),
    ]
