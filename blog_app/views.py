from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .controller import PostController  # Importing from controller.py

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/api/post/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


class PostView(APIView):

    def post(self, request):
        return PostController.create_post(request)

    def get(self, request, post_id=None):
        return PostController.get_posts(post_id)

    def put(self, request, post_id):
        return PostController.update_post(request, post_id)

    def delete(self, request, post_id):
        return PostController.delete_post(post_id)
