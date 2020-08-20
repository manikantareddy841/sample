from django.conf.urls import url
from instituteapp import views
urlpatterns=[
    url(r'^$',views.home),
    url(r'^home/',views.home),
    url(r'^contact/',views.contacts),
    url(r'^services/',views.services),
    url(r'^feedback/',views.feedbacking),
    url(r'^gallery/',views.gallery)
    ]
