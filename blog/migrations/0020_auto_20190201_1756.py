# Generated by Django 2.1.5 on 2019-02-01 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20190201_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
