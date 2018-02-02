#coding:utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import xadmin
xadmin.autodiscover()

#开启日志记录功能
#from xadmin.plugins import xversion
#xversion.register_models()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'opsx.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^', include(xadmin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
