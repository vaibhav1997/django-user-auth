# Generated by Django 2.1.5 on 2019-01-30 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190130_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imageurl',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
