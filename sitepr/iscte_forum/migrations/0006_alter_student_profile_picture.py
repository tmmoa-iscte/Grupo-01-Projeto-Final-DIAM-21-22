# Generated by Django 4.0.4 on 2022-05-11 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iscte_forum', '0005_alter_student_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_picture',
            field=models.CharField(default='iscte_forum/static/images/pfp_default.png', max_length=256),
        ),
    ]
