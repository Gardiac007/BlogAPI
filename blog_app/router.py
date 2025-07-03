from rest_framework.routers import DefaultRouter
from .views import PostView

post_router = DefaultRouter()
post_router.register(r'post', PostView) #router for post request

