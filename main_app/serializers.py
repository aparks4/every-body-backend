from rest_framework import serializers
from .models import TeamMember

class TeamMemberSerializer(serializers.HyperlinkedModelSerializer):
    edit_link = serializers.ModelSerializer.serializer_url_field(
        view_name='team_member_detail'
    )
    class Meta:
        model = TeamMember
        fields = ('name', 'bio', 'image', 'edit_link', 'id')