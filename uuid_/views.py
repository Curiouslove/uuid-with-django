from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import UUID
import uuid
from .serializers import UUIDSerializers
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import generics


# Create your views here.
class UUIDGenerator(generics.ListAPIView):
    serializer_class = UUIDSerializers
    queryset = UUID.objects.all()

    def list(self, serializer):
        uuid_var = uuid.uuid4()
        print(uuid_var)
        data = {'uuid_str': str(uuid_var)}
        serializer = UUIDSerializers(data=data)
        if serializer.is_valid():
            serializer.save()

        queryset = self.get_queryset()
        print(queryset)
        serializer2 = UUIDSerializers(queryset[::-1], many=True)
        uuids = {}
        for val in serializer2.data:
            uuids[val.get('time_stamp')] = val.get('uuid_str')
        return Response(uuids, status=status.HTTP_200_OK)
