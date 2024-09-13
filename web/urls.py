

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from news.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="home"),
    path('create_category/', CreateCategory, name='create_category'),
    path('register/', user_register, name ='create_user'),
    path('user/edit/', user_edit, name='user_edit'),
    path('password/edit/', password_edit, name='password_edit'),
    path('news_create/', createnews, name='create_news'),
    path('keraksiz/', keraksiz, name='keraksiz' ),
    path('detail/<int:id>/', detail, name='detail'),
    path('delete/<int:id>/', delete, name='delete'),
    path('edit/<int:id>/', edit, name='tahrirlash'),
    path('comment/<int:id>/<int:one>/', delete_comment, name='delete_comment'),


    path('login/', login_, name='Login'),
    path('logout/', Logout, name='logout'),

    path('yordam/', yordam, name='yordam'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
