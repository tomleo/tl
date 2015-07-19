from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    languages = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='languages'
    )
    categories = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='categories'
    )
    framework = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='framework'
    )

    class Meta:
        model = Project
        fields = ['name', 'start_date', 'end_date', 'languages', 'categories',
                  'framework']
