# Generated by Django 3.2.15 on 2022-09-29 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_congif'),
    ]

    operations = [
        migrations.AddField(
            model_name='congif',
            name='db_type',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='congif',
            name='env_name',
            field=models.TextField(null=True),
        ),
    ]
