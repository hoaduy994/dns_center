from .models import (Dns_Node_Models, Black_List_Models, 
                     White_List_Models, Log_Detail_Models, 
                     Monitor_DNS_Models, DNS_filter_Models,DnsRecordsModel,
                     DnsForwarderModel, LogToFileModel)
from .serializers import (DnsRecordsSerializer,Dns_Node_Serializer,
                          Black_List_Serializer,White_List_Serializer,
                          Log_Detail_Serializer,Monitor_DNS_Serializer,
                          DNS_filter_Serializer,UserSerializer,
                          DnsForwarderSerializer,LogToFileSerializer)
from accounts.models import CustomUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import mixins
from rest_framework import generics
from . import tasks
from support_tools import get_log_dns_node
# ###########################Dns_Node_Serializer##################################

class Dns_Node_List(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Dns_Node_Models.objects.all()
    serializer_class = Dns_Node_Serializer

class Dns_Node_Detail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Dns_Node_Models.objects.all()
    serializer_class = Dns_Node_Serializer


###########################Black_List_Serializer##################################

class Black_List(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Black_List_Models.objects.all()
    serializer_class = Black_List_Serializer



class Black_List_Detail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Black_List_Models.objects.all()
    serializer_class = Black_List_Serializer




###########################White_List_Serializer##################################

class White_List(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = White_List_Models.objects.all()
    serializer_class = White_List_Serializer

class White_List_Detail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = White_List_Models.objects.all()
    serializer_class = White_List_Serializer




###########################Log_Detail_Serializer##################################

class Log_Detail_List(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Log_Detail_Models.objects.all()
    serializer_class = Log_Detail_Serializer

class Log_Detail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Log_Detail_Models.objects.all()
    serializer_class = Log_Detail_Serializer





###########################Monitor_DNS_Serializer##################################

class Monitor_DNS_List(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Monitor_DNS_Models.objects.all()
    serializer_class = Monitor_DNS_Serializer

class Monitor_DNS_Detail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Monitor_DNS_Models.objects.all()
    serializer_class = Monitor_DNS_Serializer




###########################DNS_filter_Serializer##################################

class DNS_filter_Detail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = DNS_filter_Models.objects.all()
    serializer_class = DNS_filter_Serializer

class DNS_filter_List(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = DNS_filter_Models.objects.all()
    serializer_class = DNS_filter_Serializer

    def get(self, request, *args, **kwargs):
        
        
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = DNS_filter_Serializer(data=request.data)
        print(serializer.id)
        if serializer.is_valid():
            do_not_add_dns=""
            aaa = Dns_Node_Models.objects.all()
            add_dns=serializer.data['add_dns']
            for row in aaa:
                if str(row.id) not in add_dns:
                    do_not_add_dns+=f"{row.id}, "
            
            
            data_domain=serializer.data['data_domain']
            
            title=serializer.data['title']
            tasks.DNS_filter_List_View.delay(title=title,data_domain=data_domain,do_not_add_dns=do_not_add_dns)
        return self.create(request, *args, **kwargs)




###########################DnsRecordsModelModel##################################

class DnsRecordsModelList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = DnsRecordsModel.objects.all()
    serializer_class = DnsRecordsSerializer

class DnsRecordsModelDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = DnsRecordsModel.objects.all()
    serializer_class = DnsRecordsSerializer
##################################################################################

class UserList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    
    
###########################DnsRecordsModelModel##################################

class DnsForwarderModelList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = DnsForwarderModel.objects.all()
    serializer_class = DnsForwarderSerializer

class DnsForwarderModelDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = DnsForwarderModel.objects.all()
    serializer_class = DnsForwarderSerializer
##################################################################################


class LogToFilelList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = LogToFileModel.objects.all()
    serializer_class = LogToFileSerializer

    def get(self, request, *args, **kwargs):
        
        print("get_okila")
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        file_log=request.data['log_line']
        dns_center_id=request.data['dns_center_id']
        serializer = LogToFileSerializer(data=request.data)
        tasks.LogToFilelListView.delay(dns_center_id=dns_center_id,file_log=file_log)
        
        # get_log_dns_node.main(dns_center_id=dns_center_id,file_log=file_log)
       
       
        # with open("siem/log_line.log",'a+',encoding = 'utf-8') as f:
        #     f.write(str(file_log))
        # print(serializer.id)
        # if serializer.is_valid():
        #     do_not_add_dns=""
        #     aaa = LogToFileModel.objects.all()
        #     add_dns=serializer.data['add_dns']
        #     data_domain=serializer.data['data_domain']
            
        #     title=serializer.data['title']
        #     print(do_not_add_dns,"\n",data_domain)
            # tasks.DNS_filter_List_View.delay(title=title,data_domain=data_domain,do_not_add_dns=do_not_add_dns)
        
        return self.create(request, *args, **kwargs)

##################################################################################