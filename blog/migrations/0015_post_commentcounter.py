# Generated by Django 2.1.5 on 2019-01-31 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='commentcounter',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
