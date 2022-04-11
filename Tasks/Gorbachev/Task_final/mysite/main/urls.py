from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import os
 
urlpatterns = [
    path('', views.index, name='home'),
    path('about_us/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('posts/<int:post_id>/', views.article, name='article'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

STATIC_URL = '/static/'

STATICFILES_DIRS = [
   os.path.join(settings.BASE_DIR, "static"),
]