from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('subject/<str:category>/', views.subject_view, name='subject'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('article/<int:article_id>/update/', views.update_article, name='update_article'),
    path('article/<int:article_id>/delete/', views.delete_article, name='delete_article'),
    path('create-article/', views.create_article, name='create_article'),
    path('search/', views.search_view, name='search'),
    path('bin/', views.bin_view, name='bin'),
    path('article/<int:article_id>/restore/', views.restore_article, name='restore_article'),
    path('article/<int:article_id>/permanent-delete/', views.permanent_delete, name='permanent_delete'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
    path('terms/', views.terms_conditions, name='terms_conditions'),
]
