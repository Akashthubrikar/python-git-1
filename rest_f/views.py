from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import CastSerializer
from django.http import JsonResponse
from rest_framework import status



@api_view(["GET","POST"])
def castman(request):
    if request.method=="GET":    
        m1=cast.objects.all()
        ser=CastSerializer(m1, many=True)
        return Response(ser.data,status=status.HTTP_302_FOUND)
    if request.method=="POST":
        m1=request.data
        ser= CastSerializer(data=m1)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        


@api_view(['GET','PUT','DELETE'])
def castup(request,id):
    try:
     m2= cast.objects.get(pk=id)

    except cast.DoesNotExist:
        return Response(status==status.HTTP_404_NOT_FOUND)


    if request.method=="GET":
        ser=CastSerializer(m2)
        return Response(ser.data)

    elif request.method=="PUT":
        ser=CastSerializer(m2,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="DELETE":
        m2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)