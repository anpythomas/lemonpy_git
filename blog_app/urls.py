from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

from .views import CreatePostView

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path("index", views.index, name="index"),
    path("", views.all_posts, name="all-posts"),
    path("single_post/<slug:slug>", views.post_detail, name="single-post"),
    path("register", views.register, name="register"),
    path("login", LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name='logout'),
    path("password-change/", PasswordChangeView.as_view(), name="password-change"),
    path("password-change/done/", PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("new-post", CreatePostView.as_view(), name="new_post"),
    path("update-post/<slug:slug>", views.update_post, name="update-post"),
    path("delete-post<slug:slug>", views.delete_post, name="delete-post"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path("add-comment<slug:slug>", views.add_comment, name="add-comment"),
    path("my-likes", views.my_likes, name="my-likes"),
    path("my-comments", views.my_comments, name="my-comments"),
    path("title", views.title, name="title"),
    path("your-posts", views.your_posts, name="your-posts"),
]