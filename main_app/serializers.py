from rest_framework import serializers
from .models import TeamMember, Retreat

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
        fields = ('name', 'date', 'registration_url', 'id')