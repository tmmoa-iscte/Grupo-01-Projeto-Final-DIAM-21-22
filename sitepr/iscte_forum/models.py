from django.contrib.auth.models import User
from django.db import models

MAXIMUM_THREADS_PER_PAGE = 10
MAXIMUM_COMMENTS_PER_PAGE = 10


# ex: Licenciaturas, Mestrados, etc.
class Category(models.Model):
    # O título tem de ser Unique para se identificarem Categorias pelo título.
    title = models.CharField(max_length=50, unique=True)


# ex: Engenharia Informática, Psicologia, etc.
class Section(models.Model):
    title = models.CharField(max_length=100)
    simplified_title = models.CharField(max_length=100, unique=True)  # O título simplificado tem de ser Unique.
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    def get_number_of_pages(self):
        pages = self.thread_set.count() / MAXIMUM_THREADS_PER_PAGE
        if pages <= 1:
            return 1
        return int(pages)


# ex: Preciso de ajuda no exercício!
class Thread(models.Model):
    title = models.CharField(max_length=150)
    simplified_title = models.CharField(max_length=150)  # Pode ter o mesmo título em sections diferentes.
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    star_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField(null=True)

    def get_number_of_pages(self):
        pages = self.comment_set.count() / MAXIMUM_COMMENTS_PER_PAGE
        if pages <= 1:
            return 1
        return int(pages)


class Course(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT, null=True)
    profile_picture = models.CharField(max_length=256, default="iscte_forum/static/images/pfp_default.png")
    about_me = models.TextField(default="Gosto muito do Iscte!")
    favourite_classes = models.CharField(max_length=512, default="", null=True)


class Comment(models.Model):
    text = models.TextField()
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    time = models.DateTimeField(null=True)
    edited = models.BooleanField(default=False)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="rating_set")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="rating_set")
    positive = models.BooleanField()


class Star(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="star_set")
