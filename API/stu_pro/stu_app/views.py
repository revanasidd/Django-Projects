from .serializers import Stu_serializer
from .models import Stu_details
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def home(request):
    api_urls={
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks=Stu_details.objects.all()
    serializer=Stu_serializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createTask(request):
    serializer=Stu_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateTask(request, pk):
    task=Stu_details.objects.get(id=pk)
    serializer=Stu_serializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    task=Stu_details.objects.get(id=pk)
    serializer=Stu_serializer(task, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def taskDelete(request, pk):
    task=Stu_details.objects.get(id=pk)
    task.delete()
    return Response('item successfully deleted!')