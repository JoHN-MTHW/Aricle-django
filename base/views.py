from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Article
from django import forms
from django.db.models import Q

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserCreationForm.Meta.model
        fields = UserCreationForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def subject_view(request, category):
    articles = Article.objects.filter(category=category, is_deleted=False)
    return render(request, 'subject.html', {'articles': articles, 'category': category})

SUBJECT_CHOICES = [
    ('Science', 'Science'),
    ('History', 'History'),
    ('Literature', 'Literature'),
    ('Mathematics', 'Mathematics'),
    ('Art', 'Art'),
    ('Philosophy', 'Philosophy'),
    ('Psychology', 'Psychology'),
    ('Economics', 'Economics'),
    ('Biology', 'Biology'),
    ('Chemistry', 'Chemistry'),
    ('Physics', 'Physics'),
    ('Sociology', 'Sociology'),
    ('Geography', 'Geography'),
    ('Computer Science', 'Computer Science'),
    ('Engineering', 'Engineering'),
]

class ArticleForm(forms.ModelForm):
    category = forms.ChoiceField(choices=SUBJECT_CHOICES, widget=forms.Select())

    class Meta:
        model = Article
        fields = ['title', 'category', 'content', 'published_date', 'is_locked']

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id, is_deleted=False)
    if article.is_locked and not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'article_detail.html', {'article': article})

@login_required
def update_article(request, article_id):
    article = get_object_or_404(Article, id=article_id, is_deleted=False)
    if request.user != article.author:
        return redirect('article_detail', article_id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', article_id=article_id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'create_article.html', {'form': form})

@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id, is_deleted=False)
    if request.user != article.author:
        return redirect('article_detail', article_id=article_id)
    if request.method == 'POST':
        article.is_deleted = True
        article.save()
        return redirect('home')
    return render(request, 'article_detail.html', {'article': article, 'delete_confirm': True})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def bin_view(request):
    articles = Article.objects.filter(author=request.user, is_deleted=True)
    return render(request, 'bin.html', {'articles': articles})

@login_required
def restore_article(request, article_id):
    article = get_object_or_404(Article, id=article_id, author=request.user, is_deleted=True)
    article.is_deleted = False
    article.save()
    return redirect('bin')

@login_required
def permanent_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id, author=request.user, is_deleted=True)
    article.delete()
    return redirect('bin')

def search_view(request):
    query = request.GET.get('q', '')
    if query:
        articles = Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            is_deleted=False
        )
    else:
        articles = Article.objects.none()
    return render(request, 'search_results.html', {'articles': articles, 'query': query})

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def terms_conditions(request):
    return render(request, 'terms_conditions.html')
