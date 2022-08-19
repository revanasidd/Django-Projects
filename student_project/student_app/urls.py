from student_app import views
from django.urls import path

urlpatterns=[
    path('',views.index),
    path('path1',views.index2),
    path('path2',views.index3),
    path('path3',views.index4),
    path('path4',views.index5),
    path('path5',views.index6),
    path('path6',views.index6),
    path('path7',views.index7),
    path('path8',views.index8),
    path('path9',views.index9),
    path('htmlfile',views.htmlfile),
    path('form',views.form, name='form'),
    path('list',views.list, name='list'),
]