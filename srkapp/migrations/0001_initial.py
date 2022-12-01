# Generated by Django 4.1.3 on 2022-11-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('salary', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=300)),
                ('application_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
        migrations.CreateModel(
            name='UpdateProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(default='', max_length=50)),
                ('address1', models.CharField(default='', max_length=50)),
                ('address2', models.CharField(default='', max_length=50)),
                ('bio', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
            ],
        ),
    ]
