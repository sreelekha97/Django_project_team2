from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^StudentDetails/register/$', views.register, name ='register'),
url(r'^StudentDetails/perInfo/$', views.perInfo, name ='perInfo'),
url(r'^acadInfo/$', views.acadInfo, name ='acad'),
url(r'^addInfo/$', views.addInfo, name ='add'),
url(r'^display/$', views.display, name ='display'),
   ]
