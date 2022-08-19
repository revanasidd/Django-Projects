from django.urls import path
from Todo_app import views
urlpatterns = [
	path('',views.home,name='home'),
	path('create/',views.create_todo,name='create')

]