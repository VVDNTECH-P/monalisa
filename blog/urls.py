"""blog URL Configuration

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
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page.as_view() , name = 'home'),
    path('savecomment/<int:id>/', views.save_comments.as_view() , name = 'savecomment'),
    path('show_comment/<int:id>/', views.show_comments.as_view() , name = 'show_comment'),

    path('upload/', views.upload_post.as_view() , name = 'upload'),
    path('edit/<int:id>/', views.edit_post , name = 'edit'),
    path('delete/<int:id>/', views.delete_post.as_view() , name = 'delete'),
    path('signup/', views.sighup_form.as_view() , name = 'signin'),
    path('login/', views.login_form.as_view() , name = 'login'),
    path('logout/', views.user_logout.as_view() , name = 'logout'),
    path('information/', views.Information_view.as_view(),name='information'),
    path('delete_information/<int:id>/', views.Delete_information,name='delete_information'),
    path('otp_page/', views.Otp_page.as_view(),name = 'otp_page')








    

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


