# Generated by Django 4.0.6 on 2022-08-25 12:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 25, 12, 49, 23, 848395, tzinfo=utc)),
        ),
    ]
