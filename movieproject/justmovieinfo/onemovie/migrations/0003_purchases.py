# Generated by Django 3.0.4 on 2020-03-25 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onemovie', '0002_loginform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchesd', models.IntegerField()),
                ('users', models.IntegerField()),
            ],
        ),
    ]
