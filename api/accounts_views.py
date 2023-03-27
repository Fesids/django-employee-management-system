from django.shortcuts import render

from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from rest_framework import generics, status, permissions

from .serializers import CustomUserSerializer
from .permissions import IsAuthorOrReadOnly
from accounts.models import CustomUserModel

class CustomModeListSerializer(views.APIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = CustomUserModel.objects.all()
    serializer_class = CustomUserSerializer


    def get(self, request, *args, **kwargs):
        accounts = self.queryset.all()

        return Response({"status": "success", "accounts": self.serializer_class(accounts, many=True).data},
                        status=status.HTTP_200_OK)


class CustomModelDetailSerializer(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = CustomUserModel.objects.all()
    serializer_class = CustomUserSerializer
