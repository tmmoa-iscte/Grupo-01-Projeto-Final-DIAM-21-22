from django.urls import include, path
from . import views

app_name = 'iscte_forum'

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /register
    path('register', views.register, name='register'),
    # ex: /login
    path('login_user', views.login, name='login'),
    # ex: /profile
    path('profile', views.profile, name='profile'),
    # ex: /profile/edit
    path('profile/edit', views.profile_edit, name='profile_edit'),
    # ex: /engenharia-informatica
    path('<str:section_simplified_title>', views.section, name='section'),
    # ex: /engenharia-informatica/duvida-no-exercicio
    path('<str:section_simplified_title>/<str:thread_simplified_title>', views.thread, name='thread'),
    # ex: /engenharia-informatica/post
    path('<str:section_simplified_title>/post', views.new_thread, name='new_thread'),
    # ex: /engenharia-informatica/duvida-no-exercicio/comment
    path('<str:section_simplified_title>/<str:thread_simplified_title>/comment', views.new_comment, name='new_comment'),

]
