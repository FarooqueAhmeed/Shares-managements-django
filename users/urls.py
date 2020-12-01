from django.conf.urls import include, url
from users.views import register,login_view, logout_view
from Shares.Shares.views import index

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^index/", index, name="index"),
    url(r"^register/", register, name="register"),
    url('login',login_view, name='login'),
    url('logout', logout_view, name='logout')
    #url(r'^profile/$', profile, name='profile')
]