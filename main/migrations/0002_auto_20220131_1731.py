# Generated by Django 3.2.10 on 2022-01-31 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='temperature',
        ),
        migrations.AddField(
            model_name='weather',
            name='temp',
            field=models.CharField(default='', max_length=100),
        ),
    ]
