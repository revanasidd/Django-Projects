from .models import Employee
from .serializers import EmpSereializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET','POST'])
def empList(request):
    if request.method=='GET':
        employees=Employee.objects.all()
        serializers=EmpSereializer(instance=employees, many=True)
        return Response(serializers.data)
    else:
        serializers=EmpSereializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def emp_detail(request,id):
    try:
        employee=Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializers=EmpSereializer(instance=employee, many=False)
        return Response(serializers.data)
    elif request.method=='PUT':
        serializers=EmpSereializer(instance=employee, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)