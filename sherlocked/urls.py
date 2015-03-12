from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.contrib.auth.views import login, logout
from django.contrib.auth.models import User
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^$', 'sherlocked.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'login', 'progen.views.login', name='login'),
    url(r'register', 'progen.views.signup', name='signup'),
    url(r'profile', 'progen.views.profile', name='profile'),
    url(r'logout', 'django.contrib.auth.views.logout',{'next_page': '/login'}),
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)