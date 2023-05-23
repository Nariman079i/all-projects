from rest_framework.viewsets import ModelViewSet
from .serializers import *
from django.db.models import Q
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView, CreateAPIView
Customer

class CustomerListView(ListAPIView):
    serializer_class = CustomerSeializer

    def get_queryset(self):
        search = self.request.query_params.get('search')
        sort = self.request.query_params.get('sort')
        if search:
            return Customer.objects.filter(
                Q(surname__icontains=search) |
                Q(name__icontains=search) |
                Q(patronymic__icontains=search) |
                Q(tel__icontains=search))
        elif sort:
            return Customer.objects.all().order_by(sort)
        else:
            return Customer.objects.all()
    
class CustomerCreateView(CreateAPIView):
    serializer_class = CustomerSeializer
    queryset = Customer.objects.all()
    
class CustomerDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSeializer
    queryset = Customer.objects.all()

class ServiceListView(ListAPIView):
    serializer_class = ServiceSeializer

    def get_queryset(self):
        search = self.request.query_params.get('search')
        sort = self.request.query_params.get('sort')
        if search:
            return Service.objects.filter(
                Q(surname__icontains=search) |
                Q(name__icontains=search) |
                Q(patronymic__icontains=search) |
                Q(tel__icontains=search))
        elif sort:
            return Service.objects.all().order_by(sort)
        else:
            return Service.objects.all()
    
class ServiceCreateView(CreateAPIView):
    serializer_class = ServiceSeializer
    queryset = Service.objects.all()
    
class ServiceDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSeializer
    queryset = Service.objects.all()

class HistoryListView(ListAPIView):
    serializer_class = HistorySeializer

    def get_queryset(self):
        search = self.request.query_params.get('search')
        sort = self.request.query_params.get('sort')
        if search:
            return History.objects.filter(
                Q(surname__icontains=search) |
                Q(name__icontains=search) |
                Q(patronymic__icontains=search) |
                Q(tel__icontains=search))
        elif sort:
            return History.objects.all().order_by(sort)
        else:
            return History.objects.all()
    
class HistoryCreateView(CreateAPIView):
    serializer_class = HistorySeializer
    queryset = History.objects.all()
    
class HistoryDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = HistorySeializer
    queryset = History.objects.all()



    
class GuideListView(ListAPIView):
    serializer_class = GuideSeializer

    def get_queryset(self):
        search = self.request.query_params.get('search')
        sort = self.request.query_params.get('sort')
        if search:
            return Guide.objects.filter(
                Q(surname__icontains=search) |
                Q(name__icontains=search) |
                Q(patronymic__icontains=search) |
                Q(tel__icontains=search))
        elif sort:
            return Guide.objects.all().order_by(sort)
        else:
            return Guide.objects.all()
    
class GuideCreateView(CreateAPIView):
    serializer_class = GuideSeializer
    queryset = Guide.objects.all()
    
class GuideDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = GuideSeializer
    queryset = Guide.objects.all()

# class GuideAPIView(ModelViewSet):
#     serializer_class = GuideSeializer

#     def get_queryset(self):
#         experience = self.request.query_params('experience') 
#         salary = self.request.query_params('salary') 
#         if experience == "all" and salary == 'all':
#             return Guide.objects.all()
#         return Guide.objects.filter(Q(experience=experience) | Q(salary=salary))
