from django.urls import path, include
from .views import *

urlpatterns = [
    
    path('post/', PostView.as_view(), name='get_posts'),
    path('post/<int:post_id>/', PostView.as_view(), name='get_posts_with_id'),

    path('login/', login_view, name='login'),

] 
