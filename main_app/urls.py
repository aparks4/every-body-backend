from django.urls import path, include
from . import views



urlpatterns = [
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.TeamMemberList.as_view(), name="team_member_list"),
    path('<int:pk>/', views.TeamMemberDetail.as_view(), name="team_member_detail"),   
]