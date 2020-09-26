from apps.projects.models import Case
from rest_framework import serializers

from .models import Confirmation, Patch


class EnvoyPatchesSerializer(serializers.ModelSerializer):
    project_title = serializers.SerializerMethodField(read_only=True)

    def get_project_title(self, obj):
        project_title = ""
        if obj.project_id:
            project_title = obj.project.title
        return project_title

    class Meta:
        model = Patch
        fields = (
            "id",
            "project_title",
            "date",
            "closed",
        )
        read_only_fields = fields


class ConfirmationCaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = (
            "id",
            "name",
            "famous_name",
            "mobile",
            "address",
        )
        read_only_fields = fields


class ConfirmationInfoSerializer(serializers.ModelSerializer):
    project_title = serializers.SerializerMethodField(read_only=True)
    case = ConfirmationCaseInfoSerializer(read_only=True)

    def get_project_title(self, obj):
        project_title = ""
        if obj.project_id:
            project_title = obj.project.title
        return project_title

    class Meta:
        model = Confirmation
        fields = (
            "id",
            "project_title",
            "case",
            "delivered",
        )
        read_only_fields = fields
