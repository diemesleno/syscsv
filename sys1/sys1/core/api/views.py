from rest_framework import generics, pagination
from rest_framework.response import Response

from django_celery_results.models import TaskResult

from .serializers import ContactSerializer


class CustomPagination(pagination.PageNumberPagination):
    page_size = 100


class ContactAPIView(generics.ListAPIView):
    """ 
    API to return all messages resulted from the task queue paginated by 100
    """
    pagination_class = CustomPagination
    queryset = TaskResult.objects.all()
    serializer_class = ContactSerializer

