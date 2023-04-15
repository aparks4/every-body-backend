from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('team', views.TeamMemberList.as_view(), name="team_member_list"),
    path('team/<int:pk>', views.TeamMemberDetail.as_view(), name="team_member_detail"),
    
]