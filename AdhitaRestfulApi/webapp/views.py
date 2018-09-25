from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import car
from . serializers import carsSerializer
from .models import computer
from .serializers import computerSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import (
    SearchFilter,
    )


class carList(APIView):

    serializer_class = carsSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'color']

    def get(request, self):
        queryset = car.objects.all()
        serializer = carsSerializer(queryset, many=True)
        return Response(serializer.data)

class computerList(APIView):
    filter_backends = [SearchFilter]
    search_fields = ['computer_name', 'computer_color']

    def get(request, self):
        computers1 = computer.objects.all()
        serializer =computerSerializer(computers1, many=True)
        return Response(serializer.data)

class postList(APIView):
    queryset = car.objects.all()
    serializer_class= carsSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'color']

class carmodelList(APIView):

    def get(request, self):
        queryset = car.model_name.all()
        serializer = carsSerializer(queryset, many=True)
        return Response(serializer.data)
