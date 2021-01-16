from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from .models import LightSample
from .serializer import LightSerializer
from .permissions import PermissionsClass

# Create your views here.


class MainLight(ListAPIView):
    queryset = LightSample.objects.all()
    serializer_class = LightSerializer
    permission_classes=(PermissionsClass,)



class DetailsLight(RetrieveUpdateDestroyAPIView):
    queryset = LightSample.objects.all()
    serializer_class = LightSerializer
    permission_classes=(PermissionsClass,)



    