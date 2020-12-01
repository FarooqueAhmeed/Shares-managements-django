from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from Shares.Shares.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path(r"accounts/", include("users.urls")),
    path("",include("Shares.Shares.urls")),


]
