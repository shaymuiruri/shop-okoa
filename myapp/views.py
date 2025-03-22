from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from pymongo import MongoClient
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import viewsets
def get_collection():
    mongo_client = MongoClient(...)
    db_obj = mongo_client['ShopOkoa']
    if db_obj is not None:
        collection_obj = db_obj['ShopokoaCustomers']
        if collection_obj is not None:
            return collection_obj
    return None
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User(first_name=data['first_name'], last_name=data['last_name'], id_number=data['id_number'], phone_number=data['phone_number'], password=data['password'], tag_id=data['tag_id'], amount_saved=data['amount_save'], credit_available=data['credit_available'], trust_score_token=data['trust_score_token'], user_type=data['user_type'])
        user.save()
        return JsonResponse({"message": "User created successfully"}, status=201)

@csrf_exempt
def signin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.filter(phone_number=data['phone_number'], password=data['password'])
        if user:
            return JsonResponse({"message": "User logged in successfully"}, status=200)
        else:
            return JsonResponse({"message": "Invalid credentials"}, status=400)

class UserListView(ListView):
    model = User
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = User

class UserCreateView(CreateView):
    model = User
    fields = ['username', 'phone_number', 'password', 'tag_id', 'amount_saved', 'credit_available']
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'phone_number', 'password', 'tag_id', 'amount_saved', 'credit_available']
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = User
    context_object_name = 'user'
    success_url = reverse_lazy('user_list')

@api_view(['GET'])
def user_list(request):
    users = User.objects.all()  # Use the correct model name 'User' instead of 'user'
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer