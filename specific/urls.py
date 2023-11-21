from specific.views import *
from django.urls import path
app_name='specific'

urlpatterns=[
    path('nagaraj/',nagaraj,name='nagaraj'),
    path('chaitu/',chaitu,name='chaitu'),
]