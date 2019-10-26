from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.news_today,name='newsToday'),
    
    url(r'myaccount/', views.mine, name='myaccount'),
    url(r'^article/(\d+)',views.article,name ='article'),
    url(r'^new/article$', views.new_article, name='new-article'),

    url(r'comment/(\d+)/$', views.add_comment, name='comment'),
    url(r'myaccount/', views.mine, name='mine'),
   
    url(r'edit/', views.edit, name='edit'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'user/(?P<user_id>\d+)', views.user, name='aboutuser'),
   
    url(r'^likes/(?P<id>\d+)',views.like_it,name="like"),
    url(r'^edit/profile$',  views.edit,name='edit'),
    url(r'own_page/(\d+)', views.page, name='own_page'),
    url(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    url(r'^api/merch/$', views.MerchList.as_view()),
    url(r'^api/merchpro/$', views.MerchListpro.as_view())
    # url(r'^page/(\d+)', views.page,name=('pa')
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)