#from django.shortcuts import render
from rest_framework import viewsets
from api.models import Blog
from api.serializer import BlogSerializer
# Create your views here.
#def home(request):
#	return render(request, 'index.html')

class BlogViewSet(viewsets.ModelViewSet):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer