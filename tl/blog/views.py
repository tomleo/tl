from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from docutils.core import publish_parts

from .models import Post
from .serializers import PostSerializer, ReStructuredTextSerializer
from .permissions import IsAuthorOrReadOnly


def home(request):
    context = {
        'name': 'Tom Leo',
    }
    return render(request, 'blog/index.html', context)


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def preform_create(self, serializer):
        serializer.save(author=self.request.user)


class HTMLtoReStructuredText(APIView):

    http_method_names = [u'post']

    def post(self, request, format=None):
        rst_post = ReStructuredTextSerializer(data=request.data)
        if rst_post.is_valid():

            fin = io.StringIO()
            fin.write(rst_post.data.get('rst_file'))
            fin.seek(0)
            html_post = publish_parts(fin.read(), writer_name="html")['html_body']
            response = {
                'author': rst_post.validated_data.get('author'),
                'title': rst_post.validated_data.get('title'),
                'intro': rst_post.validated_data.get('intro'),
                'content': html_post
            }
            return Response(response)
        return Response(rst_post.errors, status=status.HTTP_400_BAD_REQUEST)