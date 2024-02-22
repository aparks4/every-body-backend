from rest_framework import serializers
from .models import TeamMember, Retreat, Resource

class TeamMemberSerializer(serializers.HyperlinkedModelSerializer):
    edit_link = serializers.ModelSerializer.serializer_url_field(
        view_name='team_member_detail'
    )
    class Meta:
        model = TeamMember
        fields = ('name', 'bio', 'image', 'edit_link', 'id')

class RetreatSerializer(serializers.HyperlinkedModelSerializer):
    edit_link = serializers.ModelSerializer.serializer_url_field(
        view_name='retreat_detail'
    )
    class Meta:
        model = Retreat
        fields = ('name', 'dates', 'image', 'description', 'registrationURL', 'edit_link', 'id')


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    edit_link = serializers.ModelSerializer.serializer_url_field(
        view_name='resource_detail'
    )
    class Meta:
        model = Resource
        fields = ('name', 'url', 'description')