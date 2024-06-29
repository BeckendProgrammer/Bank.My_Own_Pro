from django.contrib import admin
from .models import Tariffs, Tender, Transfers, Job_Openings, Products, Co_workers, Comment, Be_Co_Worker, About_Us, Joining, Individuals, Category, MainCategory, LegalEntities
# Register your models here.

@admin.register(Tariffs)
class TariffsAdmin(admin.ModelAdmin):
    list_display = ('info', 'comment', 'status', 'updated_at', 'created_at', 'id')
    list_filter =  ('status', 'updated_at', 'created_at', 'id')
    list_editable = ('status', )



@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ('tender', 'comment', 'status', 'updated_at', 'created_at', 'id')
    list_filter =  ('status', 'updated_at', 'created_at', 'id')
    list_editable = ('status', )




@admin.register(Transfers)
class TransfersAdmin(admin.ModelAdmin):
    list_display = ('co_workers', 'comment', 'status', 'updated_at', 'created_at', 'id')
    list_filter =  ('status', 'updated_at', 'created_at', 'id')
    list_editable = ('status', )




@admin.register(Job_Openings)
class Job_OpeningsAdmin(admin.ModelAdmin):
    list_display = ('about', 'openings', 'comment', 'status', 'updated_at', 'created_at', 'id')
    list_filter =  ('status', 'updated_at', 'created_at', 'id')
    list_editable = ('status', )




@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('contribution', 'plastic_cards', 'credit_cards', 'status', 'updated_at', 'created_at', 'id')
    list_filter =  ('status', 'updated_at', 'created_at', 'id')
    list_editable = ('status', )




@admin.register(Co_workers)
class Co_workersAdmin(admin.ModelAdmin):
    list_display = ('name', 'comission', 'status', 'updated_at', 'created_at', 'id')
    list_filter =  ('status', 'updated_at', 'created_at', 'id')
    list_editable = ('status', )




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'body', 'created_at', 'id')
    list_filter =  ('status', 'created_at', 'id')
    list_editable = ('status', )



@admin.register(Be_Co_Worker)
class Be_Co_WorkerAdmin(admin.ModelAdmin):
    list_display = ('joining', 'status', 'updated_at', 'created_at', 'id')
    list_filter =  ('status', 'created_at', 'id')
    list_editable = ('status', )



@admin.register(About_Us)
class About_UsAdmin(admin.ModelAdmin):
    list_display = ('information', 'status', 'updated_at', 'created_at', 'id')
    list_filter =  ('status', 'created_at', 'id')
    list_editable = ('status', )




@admin.register(Joining)
class JoiningAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'status', 'email', 'created_at', 'id')
    list_filter =  ('status', 'created_at', 'id')
    list_editable = ('status', 'email')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'status', 'news', 'created_at', 'id', 'info')
    list_filter =  ('status', 'created_at', 'id')
    list_editable = ('status',)


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at', 'id')
    list_filter =  ('status', 'created_at', 'id')
    list_editable = ('status',)



@admin.register(Individuals)
class IndividualsAdmin(admin.ModelAdmin):
    list_display = ('tariffs', 'status', 'tender', 'created_at', 'job_Openings', 'products', 'co_workers', 'comment')
    list_filter =  ('status', 'created_at')
    list_editable = ('status',)



@admin.register(LegalEntities)
class LegalEntitiesAdmin(admin.ModelAdmin):
    list_display = ('about_us', 'status', 'be_co_worker', 'created_at', 'joining')
    list_filter =  ('status', 'created_at')
    list_editable = ('status',)
