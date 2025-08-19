from django.urls import path
from . import views

urlpatterns= [
    path("", views.login_user, name="login_user"),
    path("logout", views.logout_user, name="logout_user"),
    path("index", views.index, name="index"),
    path("books", views.books,name="books"),
    path("update/<int:id>", views.update,name="update"),
    path("delete/<int:id>", views.delete,name="delete"),
]