from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from menu.models import Comuna
from .serializers import comunaSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_comunas(request):
    if request.method == 'GET':
        comuna = Comuna.objects.all()
        serializer = comunaSerializer(comuna,many=True)
        return Response(serializer.data)
    
    elif request.method =='POST':
        data = JSONParser().parse(request)
        serializer = comunaSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt
@api_view(['GET','PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_comuna(request, id):

    try:
        comuna = Comuna.objects.get(id_com = id)
    except Comuna.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = comunaSerializer(comuna)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = comunaSerializer(comuna, data=data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        comuna.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)