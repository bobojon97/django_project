from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('contact/', contact, name='contact'),
    # path('', index, name='home'),
    path('', HomePost.as_view(), name='home'),
    # path('author/<int:author_id>/', get_author, name='author'),
    path('author/<int:author_id>/', PostsAuthor.as_view(), name='author'),
    # path('post/<int:post_id>/', view_post, name='view_post'),
    path('post/<int:pk>/', ViewPost.as_view(), name='view_post'),
    # path('post/add-post/', add_post, name='add_post'),
    path('post/add-post/', CreatPost.as_view(), name='add_post'),
]