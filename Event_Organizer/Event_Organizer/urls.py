"""Event_Organizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from event_app import views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register', views.Register, name='register'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('family', views.family, name='family'),
    path('charity', views.charity, name='charity'),
    path('business', views.business, name='business'),
    path('culture', views.culture, name='culture'),
    path('contact', views.Contact_us, name='contact'),
    path('about', views.About_us, name='about'),
    path('cart', views.user_cart, name='cart'),
    path('book_event', views.bookEvent, name='book_event'),
    path('<int:id>', views.edit, name='update'),
    path('<int:id>/del', views.delete, name='delete'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)