from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)


class Section(models.Model):
    title = models.CharField(max_length=100)
    simplified_title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)


class Thread(models.Model):
    title = models.CharField(max_length=150)
    simplified_title = models.CharField(max_length=150)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    star_count = models.IntegerField()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    profile_picture = models.CharField(max_length=256, default="iscte_forum/static/images/pfp_default.png")


class Comment(models.Model):
    text = models.TextField()
    like_count = models.IntegerField()
    dislike_count = models.IntegerField()
    author = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

