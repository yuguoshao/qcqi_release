"""qcqi_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from mainpage import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('index',views.index),
    path('test',views.test),
    path('test/<int:num>', views.test, name='test'),
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
    path('seminar',views.seminar_list_web),
    path('seminar/<int:id>', views.seminar_web, name='seminar_web'),
    path('Mini-Courses',views.class_list_web),
    path('class',views.class_list_web),
    path('Mini-Courses/<int:id>', views.class_web, name='class_web'),
    path('news',views.news_list_web),
    path('news/<int:id>', views.news_web, name='news_web'),
    path('people',views.people_list_web),
    path('people/<slug:name>', views.people_web, name='people_web'),
    path('themes',views.theme_list_web),
    path('themes/<int:id>', views.theme_web, name='theme_web'),
    path('conferences',views.conference_list_web),
    path('conferences/<int:id>', views.conference_web, name='conference_web'),
    path('papers',views.papers_web),
    path('papers/<str:categroy_name>',views.papers_list_web,name='categroy_name'),
    path('about',views.about_web),
    path('',views.index),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
