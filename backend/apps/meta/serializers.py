from rest_framework import serializers

from .models import CaseType, Problem


# Case Type Info (ReadOnly) Serializer
class CaseTypeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseType
        fields = (
            "name",
            "order",
        )
        read_only_fields = fields


# Problem Info (ReadOnly) Serializer
class ProblemInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = (
            "name",
            "order",
        )
        read_only_fields = fields
