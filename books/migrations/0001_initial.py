# Generated by Django 3.0.3 on 2020-02-13 20:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('readers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('notes', models.TextField(blank=True)),
                ('has_read', models.BooleanField(default=True)),
                ('add_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('cover_img', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='readers.Reader')),
            ],
        ),
    ]
