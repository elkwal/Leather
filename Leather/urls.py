
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
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
