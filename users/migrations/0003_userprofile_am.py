# Generated by Django 3.2.8 on 2021-10-29 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='am',
            field=models.IntegerField(default='0'),
        ),
    ]