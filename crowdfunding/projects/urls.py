from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledge/<int:pk>/', views.PledgeDetail.as_view()),
    path('conditions/',views.ConditionList.as_view()),
    path('condition/<int:pk>/',views.ConditionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)