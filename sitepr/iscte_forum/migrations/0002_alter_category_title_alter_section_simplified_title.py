# Generated by Django 4.0.4 on 2022-05-06 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iscte_forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='simplified_title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]