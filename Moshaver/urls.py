from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Moshaver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/$', 'Content.views.get_all_news'),
    url(r'^workshops/$', 'Content.views.get_all_workshops'),
    url(r'^psychology/$', 'Content.views.get_all_psys'),
    url(r'^edu/$', 'Content.views.get_all_edus'),
    url(r'^news/(\d+)/$', 'Content.views.get_news'),
	# url(r'^interviews/', 'Content.views.get_all_news',
	# url(r'^FAQ/', 'Content.views.get_all_news',
    url(r'^$', 'Content.views.home_page'),
)
