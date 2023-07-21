from django.urls import path,re_path
from main_part import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Center DNS API",
      default_version='v1',
      description="☺︎☺︎☺︎☺︎☺︎☺︎",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="dangnh51@fpt.com.vn"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
   ######################################################
   path('Dns_Node_List/', views.Dns_Node_List.as_view()),
   path('Dns_Node_List/<uuid:pk>/', views.Dns_Node_Detail.as_view()),

   ######################################################
   path('Black_List/', views.Black_List.as_view()),
   path('Black_List/<uuid:pk>/', views.Black_List_Detail.as_view()),

   ######################################################
   path('White_List/', views.White_List.as_view()),
   path('White_List/<uuid:pk>/', views.White_List_Detail.as_view()),

   ######################################################
   path('Log_Detail_List/', views.Log_Detail_List.as_view()),
   path('Log_Detail_List/<uuid:pk>/', views.Log_Detail.as_view()),

   ######################################################
   path('Monitor_DNS_List/', views.Monitor_DNS_List.as_view()),
   path('Monitor_DNS_List/<uuid:pk>/', views.Monitor_DNS_Detail.as_view()),


   ######################################################
   path('DNS_filter_list/', views.DNS_filter_List.as_view()),
   path('DNS_filter_list/<uuid:pk>/', views.DNS_filter_Detail.as_view()),

   ######################################################
   path('DnsRecordsModelList/', views.DnsRecordsModelList.as_view()),
   path('DnsRecordsModelList/<uuid:pk>/', views.DnsRecordsModelDetail.as_view()),


   ######################################################
   path('users/', views.UserList.as_view()),
   path('users/<int:pk>/', views.UserDetail.as_view()),
   
   ######################################################
   path('DnsForwarderList/', views.DnsForwarderModelList.as_view()),
   path('DnsForwarderDetail/<uuid:pk>/', views.DnsForwarderModelDetail.as_view()),

   ######################################################
   path('LogToFilelList/', views.LogToFilelList.as_view()),
]