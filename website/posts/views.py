from django.shortcuts import render, Http404, HttpResponseRedirect
from .models import BlogPost
from .forms import BlogPostForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogPostSerializer
# Create your views here.



def home(request):
    context = {
    "blog_posts" : BlogPost.objects.all()
    }
    return render(request, 'home.html', context)


def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/")
            
    else:
        form = BlogPostForm()
        return render(request, 'create_post.html', {'form': form})
    



class BlogPostList(APIView):
    def get(self, request):
        blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class BlogPostDetail(APIView):
    def get_object(self, pk):
        try:
            return BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        blog_post = self.get_object(pk)
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)

    def put(self, request, pk):
        blog_post = self.get_object(pk)
        serializer = BlogPostSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        blog_post = self.get_object(pk)
        blog_post.delete()
        return Response(status=204)
