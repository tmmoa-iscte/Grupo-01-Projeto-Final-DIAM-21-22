from django.urls import include, path
from . import views

app_name = 'iscte_forum'

urlpatterns = [
    # ex: espacoiscte/
    path("", views.index, name='index'),
]
