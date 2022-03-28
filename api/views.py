from tracemalloc import BaseFilter
from warnings import filters
from django.shortcuts import render , redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import logout , login
from django.contrib.auth.hashers import make_password , check_password
from django.views.decorators.csrf import csrf_exempt

# Django Rest Filters
from rest_framework import filters
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


from rest_framework.generics import GenericAPIView , ListAPIView
from rest_framework.response import Response

from api.models import Email_log, Phone , Student
from api.serializers import PhoneSerializer , UserSerializer , StudentSerializer , EmailSerializer , LoginSerializer


# -----------------------------------------------
# DJANGO REST FILTERS


# class StudentListAPI(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     filter_backends = [DjangoFilterBackend,OrderingFilter]
#     filterset_fields = ['passby' , 'roll']
#     filterset_fields = '__all__'
#     ordering_fields = '__all__'
#     ordering = ['passby']
    
    
class StudentListAPI(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['passby' , 'roll']
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = ['passby']
    
    def get(self, request):
        serializer = self.get_serializer(self.filter_queryset(self.get_queryset()), many=True)
        return Response(serializer.data , status=200)
        
# DJANGO REST FILTER
# --------------------------------------------------------------------


# ----------------------------------------------------
class PhoneViewList(ListAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    
    def get(self, request):
        try:
            lst = request.GET.get('lst')
            print(lst)
            print(type(lst))
            lst = lst[1:-1].split(",")
            for i in range(len(lst)):
                lst[i] = int(lst[i])
            
            print(lst)
            print(type(lst))
        except :
            lst = "NULL"
      
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
        return Response(serializer.errors)

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
        return Response(serializer.errors)
    
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

class EmailAPIView(GenericAPIView):
    serializer_class = EmailSerializer
    queryset = Email_log.objects.all()
    
    def get_object(self, pk):
        try :
            return Email_log.objects.get(pk=pk)
        except Email_log.DoesNotExist :
            return None
    
    
    def get(self, request, pk=None):
        if pk :
            data = self.get_object(pk)
            if data is None:
                return Response({"Not Found" :"There is no such data in Email Database."},status=404)
            serialzer = self.get_serializer(data)
            return Response(serialzer.data , status=200)
        else :
            serializer = self.get_serializer(self.get_queryset(),many=True)
            return Response(serializer.data, status=200)
                
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            mail(request)
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

def mail(request):
    if request.method == 'POST':
        print(request.data)
        email = request.data['email']
        subject = request.data['subject']
        message = request.data['body']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject,message,email_from,recipient_list)
        print("Email sent successfully.")


# def success(request):
#     messages.success(request,request.session['msg'])
#     return render(request,'success.html')


class UserAPIView(GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def get_object(self,pk):
        try :
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None
            
    
    def get(self, request):
        # if pk :
        #     user = self.get_object(pk)
        #     if user is None :
        #         return Response({"Not Found" : "Such User does not found"} ,status=404)
        #     serializer = self.get_serializer(user)
        #     return Response(serializer.data , status=200)
        # else:
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data , status=200)
        
    def post(self, request):
        user = self.get_serializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data)
        return Response(user.errors)
        

            
# Login API
class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    # authentication_classes = [SessionAuthentication]
    
    def get_object(self , username):
        try:
            return User.objects.get(username = username)
        except User.DoesNotExist :
            return None
    
    @csrf_exempt    
    def post(self , request):
        user = self.get_object(request.data.get("username"))
        flag = check_password(request.data.get("password") , user.password)
        if not user:
            return Response({'Not Found' : 'User does not exist'} , status = 400)
        elif flag : 
            login(request , user)
            return Response({'Logged in' : 'User Logged in Successfully. '})
        else :
            return Response({'Wrong passwrd' : 'User password does not matched'} , status = 400)

# Logout API
class LogoutAPIView(GenericAPIView):
    serializer_class = LoginSerializer       
    # authentication_classes = [SessionAuthentication]
    
    def get(self , request):
        logout(request)
        return Response({'Logging out' : 'User Logged out Successfully. '})
