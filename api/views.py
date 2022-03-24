from functools import partial
from queue import Empty
from typing import List
import json
from django.shortcuts import render
from rest_framework.generics import GenericAPIView , ListAPIView
from rest_framework.response import Response
from api import serializers

from api.models import Phone
from api.serializers import PhoneSerializer , UserSerializer

# ----------------------------------------------------
class PhoneViewList(ListAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    
    def get(self, request):
        lst = request.GET['lst']
        print(type(lst))
        lst = lst[1:-1].split(",")
        for i in range(len(lst)):
            lst[i] = int(lst[i])
        
        print(lst)
        print(type(lst))
        
      
        serializer = PhoneSerializer(self.get_queryset(), many=True)
        data = {
            "serializer" : serializer.data,
            "list" : lst,
        }
        return Response(data)

# ----------------------------------------------------------
class PhoneListView(GenericAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    
    def get(self, request, lst=None):
        lst2 = request.GET.getlist('lst')
        l = None
        if lst :
            lst = request.GET.getlist('lst')
            l = lst[1:-1].split(",")
            print(type(l))
            print(l)
            for i in range(len(l)):
                try :
                    l[i] = int(l[i])
                except:
                    pass
        print(type(lst))
        print(lst)
        serializer = PhoneSerializer(self.get_queryset(), many=True)
        data = {
            "serializer" : serializer.data,
            "list" : l,
        }
        return Response(data)
        
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=201)
        return Response(serializer.error)

class PhoneDetailView(GenericAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    
    # retrieving data from db
    def get_object(self , pk):
        try:
            return Phone.objects.get(pk = pk)
        except Phone.DoesNotExist:
            return None
    
    def get(self, request, pk):
        data = self.get_object(pk)
        if not data :
            return Response({'Not Found' : 'Object does not exist'} , status = 400)
        serializer = PhoneSerializer(data)
        return Response(serializer.data)
    
    def put(self, request, pk):
        
        data = self.get_object(pk)
        if not data :
            return Response({'Not Found' : 'Object does not exist'} , status = 400)
        serializer = self.get_serializer(data , data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=201)
        return Response(serializer.error)
    
    def delete(self , request , pk):
        phone = self.get_object(pk)
        
        if not phone :
            return Response({'Not Found' : 'Object does not exist'} , status = 400)
        else:
            phone.delete()
            return Response(
                {'success' : 'Object deleted successfully !'},
                status = 200
            )

class PhoneListParams(GenericAPIView):
    serializer_class = PhoneSerializer
    queryset = Phone.objects.all()
    
    def get(self, request , lst):
        l = lst[1:-1].split(",")
        print(type(l))
        print(l)
        for i in range(len(l)):
            try :
                l[i] = int(l[i])
            except:
                pass
        
        
        return Response(l, status=200)
    