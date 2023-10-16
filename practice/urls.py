from django.urls import path, re_path
from practice import views
app_name = 'practice'

# paths for all the urls associated with practice
urlpatterns = [
    path('', views.Home, name='list'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail")
]
