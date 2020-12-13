from django.conf.urls import url

from . import views

# Url patterns for this app
    path('computegc/', ComputeGC.views.HomeView.as_view(), name='form'),
