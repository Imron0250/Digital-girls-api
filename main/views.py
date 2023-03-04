from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

@api_view(['GET'])
def info_site(request):
    info = Info.objects.last()
    ser = InfoSerializer(info, many=True)
    return Response(ser.data)

@api_view(['GET'])
def import_screen(request):
    screen = Import_screen.objects.last()
    ser = Import_screenSerializer(screen, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_about_project(request):
    about_project = About_project.objects.all()
    ser = About_projectSerializer(about_project, many=True)
    return Response(ser.data)

@api_view(['GET'])
def get_direction_about(request):
    direction_about = Direction_about.objects.all()
    ser = Direction_aboutSerializers(direction_about, many=True)
    return Response(ser.data)

@api_view(['GET'])
def get_direction_more(request):
    direction_more = Direction_more.objects.all()
    ser = Direction_moreSerializers(direction_more, many=True)
    return Response(ser.data)

@api_view(['GET'])
def get_tasks(request):
    tasks = Tasks.objects.all()
    ser = TasksSerializers(tasks, many=True)
    return Response(ser.data)

@api_view(['GET'])
def get_result(request):
    result = Result.objects.all()
    ser = ResultSerializer(result, many=True)
    return Response(ser.data)


@api_view(['POST'])
def register(request):
    name = request.POST.get('name')
    last_name = request.POST.get("last_name")
    date = request.POST.get('date')
    email = request.POST.get('email')
    adress = request.POST.get('adress')
    tel = request.POST.get('tel')
    r = Aplication.objects.create(name=name, last_name=last_name, date=date,email=email, adress=adress,tel=tel  )
    ser = AplicationSerializer(r)
    return Response(ser.data)