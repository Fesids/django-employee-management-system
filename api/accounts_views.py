from django.shortcuts import render

from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from rest_framework import generics, status

from .serializers import CustomUserSerializer
from accounts.models import CustomUserModel


class CustomUserMixin:
    queryset = CustomUserModel.objects.all()
    serializer_class = CustomUserSerializer

    '''def get_queryset(self):
        qs = super().get_queryset()
        return qs'  '''

    def get_object(self, pk):
        try:
            return CustomUserSerializer.objects.filter(id=pk)

        except:
            return Response(status.HTTP_404_NOT_FOUND)


class CustomModeListSerializer(views.APIView, CustomUserMixin):
    permission_classes = [permissions.AllowAny]


    def get(self, request, *args, **kwargs):
        accounts = self.queryset.all()

        return Response({"status": "success", "accounts": self.serializer_class(accounts, many=True).data},
                        status=status.HTTP_200_OK)
