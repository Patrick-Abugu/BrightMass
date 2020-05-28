from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

app_name= 'site'
urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'create_post/', views.create_post, name='create_post'),
    path(r'services/', views.services, name='services'),
    path(r'about/', views.about, name='about'),
    path(r'page2/', views.page2, name='page2'),
    path(r'page3/', views.page3, name='page3'),
    path(r'page4/', views.page4, name='page4'),
    path(r'feedback/', views.feedback, name = 'feedback'),
    path(r'(?P<slug>[\w-]+)/', views.post_body, name= 'details'),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
