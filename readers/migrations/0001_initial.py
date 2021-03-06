# Generated by Django 3.0.3 on 2020-02-13 20:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profile_img', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('bio', models.TextField(blank=True)),
                ('is_top', models.BooleanField(default=False)),
                ('join_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
