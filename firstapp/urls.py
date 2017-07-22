from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^snake/$',views.snake, name='snake'),
    url(r'suggestions',views.suggestions, name='suggestions'),
]
