# Generated by Django 3.2.8 on 2022-08-09 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='info',
        ),
        migrations.RemoveField(
            model_name='item',
            name='text',
        ),
    ]