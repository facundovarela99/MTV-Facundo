# Generated by Django 4.1 on 2022-08-31 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_familiares'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='profesion',
        ),
    ]
