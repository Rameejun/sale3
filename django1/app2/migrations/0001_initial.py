# Generated by Django 3.0.2 on 2020-01-05 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=30)),
                ('day', models.DateTimeField()),
                ('time1', models.DateTimeField()),
            ],
        ),
    ]
