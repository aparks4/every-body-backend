from .models import TeamMember, Retreat, ResourceCategory, Resource

from rest_framework import generics
from .serializers import TeamMemberSerializer, RetreatSerializer, ResourceCategorySerializer, ResourceSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.http import JsonResponse
# from django.contrib.auth.models import User
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.views import APIView
# from rest_framework.decorators import permission_classes
# from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
# from rest_framework import viewsets
# Create your views here.


class TeamMemberList(generics.ListCreateAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    
class TeamMemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class RetreatList(generics.ListCreateAPIView):
    queryset = Retreat.objects.all()
    serializer_class = RetreatSerializer

class RetreatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Retreat.objects.all()
    serializer_class = RetreatSerializer

class ResourceCategoryList(generics.ListCreateAPIView):
    queryset = ResourceCategory.objects.all()
    serializer_class = ResourceCategorySerializer

class ResourceCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ResourceCategory.objects.all()
    serializer_class = ResourceCategorySerializer
    
class ResourceList(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer