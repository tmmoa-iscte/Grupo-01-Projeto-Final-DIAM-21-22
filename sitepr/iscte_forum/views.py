import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.shortcuts import redirect

from .models import Student, Section, Thread, Comment, Category, Rating, Star


def index(request):
    if request.user.is_superuser and request.method == 'POST':  # 2.ª invocação. Cria a nova Section e redireciona.
        if 'new-category-title' in request.POST and request.POST['new-category-title']:
            cat = Category(title=request.POST['new-category-title'])
            cat.save()
        if 'new-sec-title' in request.POST and 'new-sec-desc' in request.POST \
                and 'new-sec-category-title' in request.POST and request.POST['new-sec-title'] \
                and request.POST['new-sec-desc'] and request.POST['new-sec-category-title']:
            # Tem dados para criar uma Section, então cria-a.
            simple_title = request.POST['new-sec-title'].lower().replace(" ", "-")
            categ = get_object_or_404(Category, title=request.POST['new-sec-category-title'])

            sec = Section(title=request.POST['new-sec-title'], simplified_title=simple_title,
                          description=request.POST['new-sec-desc'], category=categ)
            sec.save()

        return HttpResponseRedirect(reverse('iscte_forum:index'))
    else:  # 1.ª invocação. Mostra a página principal.
        return render(request, 'iscte_forum/index.html', {'all_categories': Category.objects.all()})


def register(request):
    if request.method == 'POST':  # 2.ª invocação. Cria o utilizador na BD e redireciona para o login.
        username = request.POST['user-username']
        password = request.POST['user-password']
        email = request.POST['user-email']
        course = request.POST['user-course'] if 'user_course' in request.POST else None
        about_me = request.POST['user-about-me'] if 'user-about-me' in request.POST else None
        fav = request.POST['user-favourite-classes'] if 'user-favourite-classes' in request.POST else None

        user = User.objects.create_user(username, email, password)  # Cria o User do Django.

        if 'user-profile-pic' in request.FILES:
            profile_pic_file = request.FILES['user-profile-pic']
            fs = FileSystemStorage()
            filename = fs.save(username + "_profile-picture", profile_pic_file)
            url = fs.url(filename)

            # Cria a instância de Student associada ao User criado.
            student = Student(user=user, course=course, profile_picure=url, about_me=about_me, favourite_classes=fav)
        else:
            student = Student(user=user, course=course, about_me=about_me, favourite_classes=fav)

        # Grava a informação na base de dados.
        user.save()
        student.save()

        # Redireciona o utilizador para a página de login.
        return HttpResponseRedirect(reverse('iscte_forum:login_page'))
    else:  # 1.ª invocação. Mostra a página de registo.
        return render(request, 'iscte_forum/register.html')


def login_user(request):
    if request.method == 'POST':  # 2.ª invocação. Autentica o utilizador e envia para a página principal.
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return render(request, 'iscte_forum/login.html', {'error_message': "Username ou password incorretos!", })
        return HttpResponseRedirect(reverse('iscte_forum:index'))
    else:  # 1.ª invocação. Mostra a página de login.
        return render(request, 'iscte_forum/login.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('iscte_forum:index'))


@login_required(login_url="iscte_forum:login_page")
def profile(request):
    # Mostra a página de perfil. O User pode-se ir buscar com {{ request.user }} dentro do HTML.
    return render(request, 'iscte_forum/profile.html')


@login_required(login_url="iscte_forum:login_page")
def profile_edit(request):
    if request.method == 'POST':  # 2.ª invocação. Edita o perfil e redireciona para a página de perfil.
        course = request.POST['user-course']
        about_me = request.POST['user-about-me']
        fav = request.POST['user-favourite-classes']

        student = get_object_or_404(Student, user=request.user)  # Vai buscar o Student deste User.
        student.course = course
        student.about_me = about_me
        student.fav = fav
        student.save()  # Grava a nova informação na base de dados.

        return HttpResponseRedirect(reverse('iscte_forum:profile'))  # Redireciona para a página de perfil.
    else:  # 1.ª invocação. Mostra a página de editar perfil. O User pode-se ir buscar com {{ request.user }} no HTML.
        return render(request, 'iscte_forum/profile_edit.html')


def section(request, section_simplified_title):
    # Vai buscar todas as Threads presentes nesta Section.
    threads_by_section = get_object_or_404(Section, simplified_title=section_simplified_title).thread_set.all
    return render(request, 'iscte_forum/section.html', {
        'sec': get_object_or_404(Section, simplified_title=section_simplified_title),
        'threads_by_section': threads_by_section,  # Passa a lista das threads no dicionário de contexto.
    })


def thread(request, section_simplified_title, thread_simplified_title):
    section_by_title = get_object_or_404(Section, simplified_title=section_simplified_title)
    t = get_object_or_404(Thread, section=section_by_title, simplified_title=thread_simplified_title)

    if request.method == 'POST' and 'new-comment-text' in request.POST:
        text = request.POST['new-comment-text']
        comment = Comment(text=text, author=request.user, thread=t, time=datetime.datetime.now())
        comment.save()
        return redirect_to_thread(section_simplified_title, thread_simplified_title)
    else:
        return render(request, 'iscte_forum/thread.html', {
            'section': section_by_title,
            'thread': t,
            'comments_by_thread': t.comment_set.all  # Passa a lista das threads no dicionário de contexto.
        })


@login_required(login_url="iscte_forum:login_page")
def new_thread(request, section_simplified_title):
    if request.method == 'POST':  # 2.ª invocação. Cria a nova thread e redireciona para a sua Section.
        title = request.POST['new-thread-title']
        comm = request.POST['new-thread-comment']
        simplified_title = title.lower().replace(" ", "-")

        s = get_object_or_404(Section, simplified_title=section_simplified_title)  # Vai buscar a section.

        t = Thread(title=title, simplified_title=simplified_title, section=s)  # Cria a nova Thread.
        t.save()  # Grava a nova Thread na base de dados.

        c = Comment(text=comm, author=request.user, thread=t)
        c.save()  # Grava o comentário na base de dados.

        # Estamos em, por exemplo: http://iscte-forum.pt/engenharia-informatica/action/post
        # Redireciona para, por exemplo: http://iscte-forum.pt/engenharia-informatica
        return redirect_to_thread(section_simplified_title, simplified_title)
    else:  # 1.ª invocação. Mostra a página de criar uma Thread.
        return render(request, 'iscte_forum/new_thread.html', {
            "sec": get_object_or_404(Section, simplified_title=section_simplified_title)
        })


@login_required(login_url="iscte_forum:login_page")
def rate_comment(request, section_simplified_title, thread_simplified_title, comment_id, positive_num):
    c = get_object_or_404(Comment, pk=comment_id)
    positive = True if positive_num == 1 else False  # 1 = positivo; anything else = negativo.
    r = Rating(user=request.user, comment=c, positive=positive)  # Cria o Rating.
    r.save()  # Grava o Rating na base de dados.

    return redirect_to_thread(section_simplified_title, thread_simplified_title)


@login_required(login_url="iscte_forum:login_page")
def star_thread(request, section_simplified_title, thread_simplified_title):
    s = Star(user=request.user, thread=get_thread(section_simplified_title, thread_simplified_title))
    s.save()
    return redirect_to_thread(section_simplified_title, thread_simplified_title)


# Função auxiliar — redireciona para a Thread especificada.
def redirect_to_thread(sec_simple_title, thread_simple_title):
    return HttpResponseRedirect(reverse('iscte_forum:thread', args=(sec_simple_title, thread_simple_title,)))


# Função auxiliar — devolve a thread pertencente a uma dada section.
def get_thread(section_simplified_title, thread_simplified_title):
    s = get_object_or_404(Section, simplified_title=section_simplified_title)  # Vai buscar a Section.
    return get_object_or_404(Thread, section=s, simplified_title=thread_simplified_title)  # Devolve a Thread.
