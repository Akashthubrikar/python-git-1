from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path("cast",views.castman),
    path("cast/<int:id>",views.castup)
]

urlpatterns=format_suffix_patterns(urlpatterns)