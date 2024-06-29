from django.shortcuts import render
from .models import  Tariffs, Tender, Transfers, Job_Openings, Products, Co_workers, Comment, Be_Co_Worker, About_Us, Joining, Category, MainCategory, LegalEntities, Individuals
from .serilizer import TariffsSerializer, TenderSerializer, TransfersSerializer, Job_OpeningsSerializer, ProductsSerializer, Co_workersSerializer, CommentSerializer, Be_Co_WorkerSerializer, About_UsSerializer, JoiningSerializer, MainCategorySerializer, CategorySerializer, LegalEntitiesSerializer, IndividualsSerializer

from rest_framework.response import Response
from rest_framework import viewsets, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveAPIView, ListAPIView
# Create your views here.




# """"""""""""""""""""""""""""""""""""""""""""
# Tariffs, Tender, Transfers, Job_Openings, Products, Co_workers, Comment, Be_Co_Worker, About_Us, Joining, LegalEntities, Individuals




class TariffsViewset(viewsets.ModelViewSet):
    queryset = Tariffs.objects.filter(status=True)
    serializer_class = TariffsSerializer
    permission_classes = [AllowAny]




# """"""""""""""""""""""""""""""""""""""""""""
# Tariffs, Tender, Transfers, Job_Openings, Products, Co_workers, Comment, Be_Co_Worker, About_Us, Joining, LegalEntities, Individuals



class TenderViewset(viewsets.ModelViewSet):
    queryset = Tender.objects.filter(status=True)
    serializer_class = TenderSerializer
    permission_classes = [AllowAny]





""""""""""""""""""""""""""
# Tariffs, Tender, Transfers, Job_Openings, Products, Co_workers, Comment, Be_Co_Worker, About_Us, Joining, LegalEntities, Individuals


class TransfersViewset(viewsets.ModelViewSet):
    queryset = Transfers.objects.filter(status=True)
    serializer_class = TransfersSerializer
    permission_classes = [AllowAny]




""""""""""""""""""""""""""
# Tariffs, Tender, Transfers, Job_Openings, Products, Co_workers, Comment, Be_Co_Worker, About_Us, Joining, LegalEntities, Individuals

class Job_OpeningsViewset(viewsets.ModelViewSet):
    queryset = Job_Openings.objects.filter(status=True)
    serializer_class = Job_OpeningsSerializer
    permission_classes  = [AllowAny]


   


""""""""""""""""""""
# Tariffs, Tender, Transfers, Job_Openings, Products, Co_workers, Comment, Be_Co_Worker, About_Us, Joining, LegalEntities, Individuals


class ProductsViewset(viewsets.ModelViewSet):
    queryset = Products.objects.filter(status=True)
    serializer_class = ProductsSerializer
    permission_classes = [AllowAny]



""""""""""""""""""""
# Tariffs, Tender, Transfers, Job_Openings, Products, Co_workers, Comment, Be_Co_Worker, About_Us, Joining, LegalEntities, Individuals

class Co_workersViewset(viewsets.ModelViewSet):
    queryset = Co_workers.objects.filter(status=True)
    serializer_class = Co_workersSerializer
    permission_classes = [AllowAny]



""""""""""""""""""""""""""""""""
# Tariffs, Tender, Transfers, Job_Openings, Products, Co_workers, Comment, Be_Co_Worker, About_Us, Joining, LegalEntities, Individuals

class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(status=True)
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]



""""""""""""""""""""""""""""""""""""
# Tariffs, Tender, Transfers, Job_Openings, Products, Co_workers, Comment, Be_Co_Worker, About_Us, Joining, LegalEntities, Individuals

class Be_Co_WorkerViewset(viewsets.ModelViewSet):
    queryset = Be_Co_Worker.objects.filter(status=True)
    serializer_class = Be_Co_WorkerSerializer
    permission_classes = [AllowAny]




""""""""""""""""""""""""""""""""""""""""""
# Tariffs, Tender, Transfers, Job_Openings, Products, Co_workers, Comment, Be_Co_Worker, About_Us, Joining, LegalEntities, Individuals

class About_UsViewset(viewsets.ModelViewSet):
    queryset = About_Us.objects.filter(status=True)
    serializer_class = About_UsSerializer
    permission_classes = [AllowAny]




# """"""""""""""""""""""""""""""""""""""""""""
# Tariffs, Tender, Transfers, Job_Openings, Products, Co_workers, Comment, Be_Co_Worker, About_Us, Joining, LegalEntities, Individuals




class JoiningViewset(viewsets.ModelViewSet):
    queryset = Joining.objects.filter(status=True)
    serializer_class = JoiningSerializer
    permission_classes = [AllowAny]




# """"""""""""""""""""""""""""""""""""""""""""
# Tariffs, Tender, Transfers, Job_Openings, Products, Co_workers, Comment, Be_Co_Worker, About_Us, Joining, LegalEntities, Individuals




class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=True)
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]



# # """"""""""""""""""""""""""""""""""""""""""""
# # Tariffs, Tender, Transfers, Job_Openings, Products, Co_workers, Comment, Be_Co_Worker, About_Us, Joining, LegalEntities, Individuals




class MainCategoryViewset(viewsets.ModelViewSet):
    queryset = MainCategory.objects.filter(status=True)
    serializer_class = MainCategorySerializer
    permission_classes = [AllowAny]




""""""""""""""""""""""""""""""""""""""""""
# Tariffs, Tender, Transfers, Job_Openings, Products, Co_workers, Comment, Be_Co_Worker, About_Us, Joining, LegalEntities, Individuals

class LegalEntitiesViewset(viewsets.ModelViewSet):
    queryset = LegalEntities.objects.filter(status=True)
    serializer_class = LegalEntitiesSerializer
    permission_classes = [AllowAny]





""""""""""""""""""""""""""""""""""""""""'"""
# Tariffs, Tender, Transfers, Job_Openings, Products, Co_workers, Comment, Be_Co_Worker, About_Us, Joining, LegalEntities, Individuals

class IndividualsViewset(viewsets.ModelViewSet):
    queryset = Individuals.objects.filter(status=True)
    serializer_class = IndividualsSerializer
    permission_classes = [AllowAny]


























































# 
# w
# # q
# # # class TariffsApiListview(ListAPIView):
# # #     queryset = Tariffs.objects.filter(status=True)
# # #     serializer_class = TariffsApiSerializer
# # #     permission_classes = [AllowAny]

# # # class TenderApiListview(ListAPIView):
# # #     queryset = Tender.objects.filter(status=True)
# # #     serializer_class = TenderApiSerializer
# # #     permission_classes = [AllowAny]

# # # class TransfersApiListview(ListAPIView):
# # #     queryset = Transfers.objects.filter(status=True)
# # #     serializer_class = TransfersApiSerializer
# # #     permission_classes = [AllowAny]

# # # class Job_OpeningsApiListview(ListAPIView):
# # #     queryset = Job_Openings.objects.filter(status=True)
# # #     serializer_class = Job_OpeningsApiSerializer
# # #     permission_classes = [AllowAny]

# # # class ProductsApiListview(ListAPIView):
# # #     queryset = Products.objects.filter(status=True)
# # #     serializer_class = ProductsApiSerializer
# # #     permission_classes = [AllowAny]

# # # class Co_workersApiListview(ListAPIView):
# # #     queryset = Co_workers.objects.filter(status=True)
# # #     serializer_class = Co_workersApiSerializer
# # #     permission_classes = [AllowAny]

# # # class CommentApiListview(ListAPIView):
# # #     queryset = Comment.objects.filter(status=True)
# # #     serializer_class = CommentApiSerializer
# # #     permission_classes = [AllowAny]

# # # class Be_Co_WorkerApiListview(ListAPIView):
# # #     queryset = Be_Co_Worker.objects.filter(status=True)
# # #     serializer_class = Be_Co_WorkerApiSerializer
# # #     permission_classes = [AllowAny]

# # # class About_UsApiListview(ListAPIView):
# # #     queryset = About_Us.objects.filter(status=True)
# # #     serializer_class = About_UsApiSerializer
# # #     permission_classes = [AllowAny]

# # # class JoiningApiListview(ListAPIView):
# # #     queryset = Joining.objects.filter(status=True)
# # #     serializer_class = JoiningApiSerializer
# # #     permission_classes = [AllowAny]

# # # class LegalEntitiesApiListview(ListAPIView):
# # #     queryset = LegalEntities.objects.filter(status=True)
# # #     serializer_class = LegalEntitiesApiSerializer
# # #     permission_classes = [AllowAny]

# # # class IndividualsApiListview(ListAPIView):
# # #     queryset = Individuals.objects.filter(status=True)
# # #     serializer_class = IndividualsApiSerializer
# # #     permission_classes = [AllowAny]











































# # # class TariffsApiDetailview(RetrieveAPIView):
# # #     queryset = Tariffs.objects.filter(status=True)
# # #     serializer_class = TariffsApiSerializer
# # #     permission_classes = [AllowAny]
# # #     lookup_field = 'slug'

# # # class TenderApiDetailview(RetrieveAPIView):
# # #     queryset = Tender.objects.filter(status=True)
# # #     serializer_class = TenderApiSerializer
# # #     permission_classes = [AllowAny]
# # #     lookup_field = 'slug'

# # # class TransfersApiDetailview(RetrieveAPIView):
# # #     queryset = Transfers.objects.filter(status=True)
# # #     serializer_class = TransfersApiSerializer
# # #     permission_classes = [AllowAny]
# # #     lookup_field = 'slug'

# # # class Job_OpeningsApiDetailview(RetrieveAPIView):
# # #     queryset = Job_Openings.objects.filter(status=True)
# # #     serializer_class = Job_OpeningsApiSerializer
# # #     permission_classes = [AllowAny]
# # #     lookup_field = 'slug'

# # # class ProductsApiDetailview(RetrieveAPIView):
# # #     queryset = Products.objects.filter(status=True)
# # #     serializer_class = ProductsApiSerializer
# # #     permission_classes = [AllowAny]
# # #     lookup_field = 'slug'

# # # class Co_workersApiDetailview(RetrieveAPIView):
# # #     queryset = Co_workers.objects.filter(status=True)
# # #     serializer_class = Co_workersApiSerializer
# # #     permission_classes = [AllowAny]
# # #     lookup_field = 'slug'

# # # class CommentApiDetailview(RetrieveAPIView):
# # #     queryset = Comment.objects.filter(status=True)
# # #     serializer_class = CommentApiSerializer
# # #     permission_classes = [AllowAny]
# # #     lookup_field = 'slug'

# # # class Be_Co_WorkerApiDetailview(RetrieveAPIView):
# # #     queryset = Be_Co_Worker.objects.filter(status=True)
# # #     serializer_class = Be_Co_WorkerApiSerializer
# # #     permission_classes = [AllowAny]
# # #     lookup_field = 'slug'

# # # class About_UsApiDetailview(RetrieveAPIView):
# # #     queryset = About_Us.objects.filter(status=True)
# # #     serializer_class = About_UsApiSerializer
# # #     permission_classes = [AllowAny]
# # #     lookup_field = 'slug'

# # # class JoiningApiDetailview(RetrieveAPIView):
# # #     queryset = Joining.objects.filter(status=True)
# # #     serializer_class = JoiningApiSerializer
# # #     permission_classes = [AllowAny]
# # #     lookup_field = 'slug'

# # # class LegalEntitiesApiDetailview(RetrieveAPIView):
# # #     queryset = LegalEntities.objects.filter(status=True)
# # #     serializer_class = LegalEntitiesApiSerializer
# # #     permission_classes = [AllowAny]
# # #     lookup_field = 'slug'

# # # class IndividualsApiDetailview(RetrieveAPIView):
# # #     queryset = Individuals.objects.filter(status=True)
# # #     serializer_class = IndividualsApiSerializer
# # #     permission_classes = [AllowAny]
# # #     lookup_field = 'slug'









