
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns=[
    url(r'^$',views.index,name='indexPage'),
    url(r'^group/',views.group,name='group'),
    url(r'^allbiz/',views.allbiz,name='allbiz'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^upload/',views.upload, name='upload'),
    url('profile/$', views.profile, name='profile'),
    url('^town/(\w+)', views.town, name='town'),
    url('update/$', views.update, name='update'),
    url('^new_town/$', views.new_town, name='new_town'),
    url('^join/(\d+)', views.join, name='join'),
    url('^all_towns/$',views.all_towns,name='all_towns'),
    url('^comment/(\d+)', views.comment, name='comment'),
    url('^new_post/$', views.new_post, name='new_post'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
