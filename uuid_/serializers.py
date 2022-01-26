from django.db.models.fields import Field
from rest_framework import serializers
from .models import UUID


class UUIDSerializers(serializers.ModelSerializer):

    class Meta:
        model = UUID
        fields = ("uuid_str", "time_stamp")
