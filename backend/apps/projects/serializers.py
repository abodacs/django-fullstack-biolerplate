from apps.meta.serializers import CaseTypeInfoSerializer, ProblemInfoSerializer
from rest_framework import serializers

from .models import Case


# Case Serializer
class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = (
            "id",
            "name",
            "code",
            "famous_name",
            "mobile",
            "address",
            "national_id",
            "description",
            "types",
            "problems",
        )


class CaseInfoSerializer(serializers.ModelSerializer):
    types = CaseTypeInfoSerializer(many=True, read_only=True)
    problems = ProblemInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Case
        fields = (
            "id",
            "name",
            "code",
            "famous_name",
            "mobile",
            "address",
            "national_id",
            "description",
            "types",
            "problems",
        )
        read_only_fields = fields
