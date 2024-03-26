from django.urls import path, include
from . import views



urlpatterns = [
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.TeamMemberList.as_view(), name="team_member_list"),
    path('<int:pk>/', views.TeamMemberDetail.as_view(), name="team_member_detail"), 
    path('retreats', views.RetreatList.as_view(), name="retreat_list"),
    path('retreats/<int:pk>/', views.RetreatDetail.as_view(), name="retreat_detail"),
    path('resources', views.ResourceList.as_view(), name="resource_list"),
    path('resources/<int:pk>/', views.ResourceDetail.as_view(), name="resource_detail"),
    path('resource_categories', views.ResourceCategoryList.as_view(), name="resource_category_list"),
    path('resource_categories/<int:pk/', views.ResourceCategoryDetail.as_view(), name="resource_category_detail"),
     
]