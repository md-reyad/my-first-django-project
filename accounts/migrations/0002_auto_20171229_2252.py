# Generated by Django 2.0 on 2017-12-29 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='updated_at',
        ),
    ]
