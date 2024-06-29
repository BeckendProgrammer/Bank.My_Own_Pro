from creditapp.models import Tariffs, Tender, Transfers, Job_Openings, Products, Co_workers, Comment, Be_Co_Worker, About_Us, Joining, Category, MainCategory, Individuals, LegalEntities
from rest_framework import serializers


class TariffsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tariffs
        fields = ('info', 'comment')

class TenderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tender
        fields = ('tender','comment')


class TransfersSerializer(serializers.ModelSerializer):
    class Meta:
        model= Transfers
        fields = ('co_workers','comment')


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('plastic_cards','credit_cards','contribution')


class Co_workersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Co_workers
        fields = ('name','comission')


class Be_Co_WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Be_Co_Worker
        fields = ('joining',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name','email','body')



class About_UsSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_Us
        fields = ('information',)



class JoiningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joining
        fields = ('full_name','email')



class Job_OpeningsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Openings
        fields = ('about', 'openings', 'comment')



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category','info','news')



class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = ('name',)



class LegalEntitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalEntities
        fields = ('about_us','be_co_worker','joining')



class IndividualsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individuals
        fields = ('tender','co_workers','products','transfers','tariffs','job_Openings','comment')










""" API """

# Tariffs, Tender, Transfers, Job_Openings, Products, Co_workers, Comment, Be_Co_Worker, About_Us, Joining









class TariffsApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariffs
        fields = ('info', 'comment')



class TenderApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tender
        fields = ('tender', 'comment')



class TransfersApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfers
        fields = ('co_workers', 'comment')



class Job_OpeningsApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Openings
        fields = ('about', 'openings', 'comment')


class ProductsApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('plastic_cards', 'credit_cards', 'contribution')



class Co_workersApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Co_workers
        fields = ('name', 'comission')



class CommentApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')



class Be_Co_WorkerApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Be_Co_Worker
        fields = ('joining', )



class About_UsApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_Us
        fields = ('information', )



class JoiningApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joining
        fields = ('full_name', 'email')



class IndividualsApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individuals
        fields = ('tariffs', 'job_openings', 'transfers', 'products', 'co_workers', 'tender')



class LegalEntitiesApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalEntities
        fields = ('about_us', 'be_co_worker', 'joining')
