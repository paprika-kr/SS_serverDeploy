from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from secondstep.vision_api import *
from secondstep.getdata import *
# Create your views here.
@api_view(['GET'])
def printObject(id):
    title = localize_objects(r"C:\Users\Figure\Desktop\cd1\test\dog.jpg")
    obj = objectMatcher(title)
    serializer = ObjectSerializer(obj)
    return Response(serializer.data)

@api_view(['GET'])
def helloAPI(request):
    return Response("hello world")

