# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all', views.all, name="all" ),
    path('login', views.login, name="login" ),
    path('signup', views.signup, name="signup"),
    path('problems', views.problems, name="problems"),
    path('addproblem', views.addproblem, name="addproblem"),
    path('delete/<int:id>', views.delete)

]