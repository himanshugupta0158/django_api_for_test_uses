from sqlite3 import converters
from django.urls import path , register_converter
from api import views
from api import converters




# register_converter(converters.listmaintainer, 'list')

urlpatterns = [
    # path('',views.PhoneListView.as_view()),
    
    path('',views.PhoneViewList.as_view()),
    
    
    path('<int:pk>',views.PhoneDetailView.as_view()),
    path('param/<lst>',views.PhoneListParams.as_view()),
    
]
