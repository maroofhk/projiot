from django.conf.urls import patterns, include, url
from django.contrib import admin

# ------------------ login commentout
# from device.views import *
from device import views as devView
# ------------------ login commentout

# ------------------ login addition
from index import views as indexView
# ------------------ login addition

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projiot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^devices/all/', devView.all_devices),
    url(r'^nurses/all/', devView.all_nurses),
    url(r'^device/details/(?P<pk>[0-9]+)/$', devView.device_details),
    url(r'^device/state/change/', devView.update_device_state),
    url(r'^nurses/$', devView.nurse_list),
    
    # ------------------ login commentout
    # url(r'^$', devView.home),
    # ------------------ login commentout
    
    url(r'^device/add/$', devView.home),
    url(r'^devices/$', devView.device_list),
    
    url(r'^login/$', indexView.Login),
    url(r'^logout/$', indexView.Logout),
    # url(r'^home/$', indexView.Home),
    
    #=========================================
    # url(r'^$', indexView.Home),
    url(r'^$', indexView.Login),
    #=========================================
    #url(r'^$', indexView.Login),
    
    # url(r'^blog/$', views.Blog),
    # ------------------ login addition
)
