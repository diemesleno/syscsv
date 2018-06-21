from rest_framework.views import APIView
from rest_framework.response import Response

from django_celery_results.models import TaskResult

from .serializers import ContactSerializer


class ContactAPIView(APIView):
    """ 
    API to return all messages resulted from the task queue
    """
    def get(self, request, format=None):
        qs = TaskResult.objects.all()
        serializer = ContactSerializer(qs, many=True)
        return Response(serializer.data)
