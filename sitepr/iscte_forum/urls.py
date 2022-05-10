from django.urls import include, path
from . import views
# (. significa que importa views da mesma directoria)

app_name = 'iscte_forum'

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /register
    path('register', views.register, name='register'),
    # ex: /login
    path('login', views.login_user, name='login_page'),
    # ex: /logout
    path('logout', views.logout_user, name='logout_page'),
    # ex: /profile
    path('profile', views.profile, name='profile'),
    # ex: /profile/edit
    path('profile/edit', views.profile_edit, name='profile_edit'),
    # ex: /engenharia-informatica
    path('<str:section_simplified_title>', views.section, name='section'),
    # ex: /engenharia-informatica/duvida-no-exercicio
    path('<str:section_simplified_title>/<str:thread_simplified_title>', views.thread, name='thread'),
    # ex: /engenharia-informatica/post
    path('<str:section_simplified_title>/action/post', views.new_thread, name='new_thread'),

    # ex: /engenharia-informatica/duvida-no-exercicio/7/1 (1 = positivo; anything else = negativo.)
    path('<str:section_simplified_title>/<str:thread_simplified_title>/<int:comment_id>/<int:positive_num>',
         views.rate_comment, name='rate_comment'),
    # ex: /engenharia-informatica/duvida-no-exercicio/star
    path('<str:section_simplified_title>/<str:thread_simplified_title>/star', views.star_thread, name='star_thread'),
]
