# Generated by Django 4.1.3 on 2022-11-30 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('srkapp', '0005_resume_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='spec',
        ),
    ]