# Generated by Django 3.2.8 on 2021-10-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_auto_20211028_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(blank=True, max_length=58, null=True),
        ),
    ]