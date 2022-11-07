from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response


from financepeer.models import UserModel
from financepeer.serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        payload = request.data
        # serializer = UserSerializer(data=[payload])
        # if serializer.is_valid():
        #         print('saved')
        #         serializer.save()
        #         return Response("Data Saved successfully")
        # else:
        #     print('err', serializer.errors)
        #     return Response(serializer.errors)
        
        print("payload",payload)
        for obj in payload:
            print("obj",obj)            
            serializer = UserSerializer(data=obj)
            if serializer.is_valid():
                print('saved')
                serializer.save()
            else:
                print('err', serializer.errors)
                return Response(serializer.errors)
        queryset = UserModel.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
