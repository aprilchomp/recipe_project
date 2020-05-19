from django.urls import path
from . import views

urlpatterns = [
    	path('', views.index),
		path('register', views.register),
		path('login', views.login),
		path('search', views.search),
		path('search_recipe', views.search_recipe),
		path('result', views.result),
		path('profile', views.profile),
		path('logout', views.logout),
		path('save_recipe', views.save_recipe),
		path('enternewtemplate', views.enternewtemplate),
		path('enternew', views.enternew),
]
