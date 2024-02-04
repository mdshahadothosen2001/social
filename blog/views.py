from rest_framework import generics
from .serializer import PostSerializer
from .models import Post

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView




class CreatePostView(APIView):
    """Create a new blog post."""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """Create a new blog post."""
        title = request.data.get("title")
        content = request.data.get("content")

        if title is None or content is None:
            return Response(
                {"error": "You must provide both title and content fields."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        post_data = {"title": title, "content": content}

        serializer = PostSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Successfully created a new blog post."},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"error": "Invalid data. Please check your input."},
                status=status.HTTP_400_BAD_REQUEST,
            )



class PostList(generics.ListCreateAPIView):
    """This class handles listing and creating posts using Django Rest Framework"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        """List all blog posts in a custom JSON format"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Manually construct the response JSON data
        response_data = {
            "status": "success",
            "message": "Successfully retrieved all blog posts.",
            "data": serializer.data,
        }

        return Response(response_data, status=status.HTTP_200_OK)