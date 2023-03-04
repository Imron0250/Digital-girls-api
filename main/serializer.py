from rest_framework import serializers
from .models import *


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"

class Import_screenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Import_screen
        fields = "__all__"


class About_projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_project
        fields = "__all__"


class Direction_moreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Direction_more
        fields = "__all__"

class Direction_aboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = Direction_about
        fields = "__all__"

class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"

class AplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aplication
        fields = "__all__"