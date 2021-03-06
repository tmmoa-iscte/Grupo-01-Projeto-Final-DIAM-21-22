# Generated by Django 4.0.4 on 2022-04-23 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('simplified_title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='iscte_forum.category')),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('simplified_title', models.CharField(max_length=150)),
                ('star_count', models.IntegerField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscte_forum.section')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
                ('profile_picture', models.CharField(default='iscte_forum/static/images/pfp_default.png', max_length=256)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('like_count', models.IntegerField()),
                ('dislike_count', models.IntegerField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='iscte_forum.student')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscte_forum.thread')),
            ],
        ),
    ]
