# Generated by Django 2.0.1 on 2018-01-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concussiontest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='base_errors',
            field=models.IntegerField(default=0),
        ),
    ]