from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings

from . import views
from .forms import LoginForm

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login', kwargs={'template_name': 'accounts/login.html',
                                                             'authentication_form': LoginForm,}),
    url(r'^logout/$', auth_views.logout, name='logout', kwargs={'next_page': settings.LOGIN_URL}),
    url(r'profile/$', views.profile, name='profile'),
    url(r'^signup/$', views.signup, name='signup'),
]