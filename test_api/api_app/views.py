from .serializers import empSerializer
from .models import Employee
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def emp_list(request):
    emp=Employee.objects.all()
    serializer=empSerializer(emp, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def emp_create(request):
    serializer=empSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_emp(request, id):
    emp=Employee.objects.get(pk=id)
    serializer=empSerializer(emp, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data,status=status.HTTP_200_SUCCESS)

@api_view(['GET'])
def delete_emp(request, id):
    emp=Employee.objects.get(pk=id)
    emp.delete()
    return Response('Employee successfully deleted')