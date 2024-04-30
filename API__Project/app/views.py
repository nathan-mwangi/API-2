from django.shortcuts import render
from django.http import JsonResponse
from .models import Brand
from .serializers import BrandSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def getbrand(request, format=None):
    if request.method == 'GET':
        Products = Brand.objects.all()
        serializer = BrandSerializer(Products, many=True)
        return Response(serializer.data)