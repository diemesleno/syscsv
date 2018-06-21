from django.urls import path


from .views import TaskResultAPIView

urlpatterns = [
    path('', TaskResultAPIView.as_view(), name='index'),
]