from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()
urlpatterns = [
    # Examples:
    # url(r'^$', 'Moshaver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^news/$', 'Content.views.get_all_news'),
    url(r'^news/(\d+)/$', 'Content.views.get_news'),

    url(r'^workshops/$', 'Content.views.get_all_workshops'),
    url(r'^workshops/(\d+)/$', 'Content.views.get_workshop'),
    
    url(r'^psychology/$', 'Content.views.get_all_psys'),
    url(r'^psychology/(\d+)/$', 'Content.views.get_psy'),

    url(r'^edu/$', 'Content.views.get_all_edus'),
    url(r'^edu/(\d+)/$', 'Content.views.get_edu'),

    url(r'^faq/$', 'Content.views.get_all_faqs'),
    
    url(r'^gallery/$', 'Content.views.get_gallery'),
    url(r'^graduates/$', 'Content.views.get_all_grads'),
    url(r'^advisors/$', 'Content.views.get_all_advisors'),

    url(r'^$', 'Content.views.home_page'),
]