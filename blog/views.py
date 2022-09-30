from ast import If
from django.http import JsonResponse
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def blog_list(request, format=None):
    if request.method == 'GET':
        #Get all the drinks
        blogs = Blog.objects.all()

        #serialze them
        serialzer = BlogSerializer(blogs, many=True)

        #return json
        return JsonResponse({"blogs": serialzer.data})

    if request.method == 'POST':
        serialzer = BlogSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def blog_details(request, id, format=None):
    try:
        blog = Blog.objects.get(pk=id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =  BlogSerializer(blog)
        return JsonResponse(serializer.data)
 
    if request.method == 'PUT':
        serializer =  BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 