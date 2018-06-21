from rest_framework import generics, pagination
from rest_framework.views import APIView
from rest_framework.response import Response

from django_celery_results.models import TaskResult
from .serializers import TaskResultSerializer


class CustomPagination(pagination.PageNumberPagination):
    page_size = 100
 

class TaskResultAPIView(generics.ListAPIView):
    """ 
    API to return all messages resulted from the task queue paginated by 100
    """
    pagination_class = CustomPagination
    queryset = TaskResult.objects.all().order_by('id')
    serializer_class = TaskResultSerializer

    def get_paginated_response(self, data):
        paginate = bool(self.request.GET.get('paginate', None))
        if paginate:
            serializer = TaskResultSerializer(self.queryset.all(), many=True, context={'request': self.request})
            response = Response(serializer.data, status=200)
            return response
        return self.paginator.get_paginated_response(data)
