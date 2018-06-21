from rest_framework import serializers

from django_celery_results.models import TaskResult


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskResult
        fields = [
            'result'
        ]
