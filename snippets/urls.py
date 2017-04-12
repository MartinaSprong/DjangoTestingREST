from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    # url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/$', views.jsonGetChlorosity),
]

urlpatterns = format_suffix_patterns(urlpatterns)



