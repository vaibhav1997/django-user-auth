# Generated by Django 2.1.5 on 2019-01-30 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190130_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imageurl',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
