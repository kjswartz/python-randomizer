from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

def index(_):
    return HttpResponse("Hello, world. You're at the api index.")

class BlogPostListCreate(generics.ListCreateAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializer

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializer
  lookup_field = "pk"
