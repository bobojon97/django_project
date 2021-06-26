from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author
from .forms import PostForm, UserRegisterForm, UserLoginForm, ContactForm
from django.views.generic import ListView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import  send_mail

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'simpleApp/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'simpleApp/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'bobojon-999@yandex.ru', 
            ['rbobojon1@gmail.com'], fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('contact')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка валидации')
    else:
        form = ContactForm()
    return render(request, 'simpleApp/test.html', {'form': form})

class HomePost(ListView):
    model = Post
    template_name = 'simpleApp/home_post.html'
    context_object_name = 'post'
    queryset = Post.objects.select_related('name')
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

class PostsAuthor(ListView):
    model = Post
    template_name = 'simpleApp/home_post.html'
    context_object_name = 'post'
    allow_empty = False
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(name_id=self.kwargs['author_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Author.objects.get(pk=self.kwargs['author_id'])
        return context

class ViewPost(DeleteView):
    model = Post
    template_name = 'simpleApp/post_confirm_delete.html'
    context_object_name = 'post_item'
    # pk_url_kwarg = 'post_id'

class CreatPost(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'simpleApp/add_post.html'
    # login_url = '/admin/'
    raise_exception = True

# def index(request):
#     post = Post.objects.all()
#     context = {
#         'post': post,
#         'title': 'Список тасков',
#     }
#     return render(request, 'simpleApp/index.html', context)

# def get_author(request, author_id):
#     post = Post.objects.filter(name_id=author_id)
#     author = Author.objects.get(pk=author_id)
#     return render(request, 'simpleApp/author.html', {'post': post,  'author': author})

# def view_post(request, post_id):
#     # post_item = Post.objects.get(pk=post_id)
#     post_item = get_object_or_404(Post, pk=post_id)
#     return render(request, 'simpleApp/view_post.html', {'post_item': post_item})

# def add_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # post = Post.objects.create(**form.cleaned_data)
#             post = form.save()
#             return redirect(post)
#     else:
#         form = PostForm()
#     return render(request, 'simpleApp/add_post.html', {'form': form})

