from django.urls import path 
from.views import PostView,CreatePostView


urlpatterns = [
    path('create/', CreatePostView.as_view(), name="create-post"),
    path('view/', PostView.as_view(), name="view-post"),
]
