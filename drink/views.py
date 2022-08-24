from ast import If
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    if request.method == 'GET':
        #Get all the drinks
        drinks = Drink.objects.all()

        #serialze them
        serialzer = DrinkSerializer(drinks, many=True)

        #return json
        return JsonResponse({"drinks": serialzer.data})

    if request.method == 'POST':
        serialzer = DrinkSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_details(request, id, format=None):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =  DrinkSerializer(drink)
        return JsonResponse(serializer.data)
 
    if request.method == 'PUT':
        serializer =  DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 