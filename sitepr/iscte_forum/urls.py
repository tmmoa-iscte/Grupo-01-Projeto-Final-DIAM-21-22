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
    # ex: /profile/2
    path('profile/<str:username>', views.profile, name='profile'),
    # ex: /profile/edit
    path('profile/<str:username>/edit', views.profile_edit, name='profile_edit'),
    # ex: /engenharia-informatica
    path('<str:section_simplified_title>', views.section, name='section'),
    # ex: /engenharia-informatica/duvida-no-exercicio
    path('<str:section_simplified_title>/<str:thread_simplified_title>', views.thread, name='thread'),
    # ex: /engenharia-informatica/action/post
    path('<str:section_simplified_title>/action/post', views.new_thread, name='new_thread'),
    # ex: /engenharia-informatica/duvida-no-exercicio/action/delete
    path('<str:section_simplified_title>/<str:thread_simplified_title>/action/delete', views.delete_thread,
         name="delete_thread"),
    # ex: /Licenciaturas/action/delete
    path('categories/action/delete', views.delete_category, name='delete_category'),
    # ex: /engenharia-informatica/action/delete
    path('<str:section_simplified_title>/action/delete', views.delete_section, name='delete_section'),

    # ex: /engenharia-informatica/duvida-no-exercicio/7/1 (1 = positivo; anything else = negativo.)
    path('<str:section_simplified_title>/<str:thread_simplified_title>/<int:comment_id>/<int:positive_num>',
         views.rate_comment, name='rate_comment'),
    # ex: /engenharia-informatica/duvida-no-exercicio/7/edit
    path('<str:section_simplified_title>/<str:thread_simplified_title>/<int:comment_id>/edit',
         views.edit_comment, name='edit_comment'),
    # ex:
    path('<str:section_simplified_title>/<str:thread_simplified_title>/<int:comment_id>/delete', views.delete_comment,
         name='delete_comment'),
    # ex: /engenharia-informatica/duvida-no-exercicio/star
    path('<str:section_simplified_title>/<str:thread_simplified_title>/star', views.star_thread, name='star_thread'),
]
