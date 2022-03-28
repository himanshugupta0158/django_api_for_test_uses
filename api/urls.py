from sqlite3 import converters
from django.urls import path , register_converter
from api import views
from api import converters




# register_converter(converters.listmaintainer, 'list')

urlpatterns = [
    # path('',views.PhoneListView.as_view()),
    
    path('phone',views.PhoneViewList.as_view()),
    
    
    path('phone/<int:pk>',views.PhoneDetailView.as_view()),
    path('param/<lst>',views.PhoneListParams.as_view()),
    path('email/',views.EmailAPIView.as_view()),
    path('email/<int:pk>',views.EmailAPIView.as_view()),
    path('user/',views.UserAPIView.as_view()),
    path('login/',views.LoginAPIView.as_view()),
    path('logout/',views.LogoutAPIView.as_view()),
    path('student/',views.StudentListAPI.as_view()),
    
]
