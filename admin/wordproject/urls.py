from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from wordproject import views

urlpatterns = [
    url(r'^wordRecords/$', views.WordRecordList.as_view()),
    url(r'^wordRecords/(?P<pk>[0-9]+)/$', views.WordRecordDetail.as_view()),
    url(r'^wordRecords/Filter/(?P<englishWord>.+)/$', views.WordRecordFilteredList.as_view()),
    url(r'^wordRecords/Search/$', views.WordRecordQueryParamList.as_view()),
    url(r'^wordPair/$', views.WordPairList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
