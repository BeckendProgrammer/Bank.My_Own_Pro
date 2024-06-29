from django.urls import path, include
from rest_framework import routers
from .views import TariffsViewset, TenderViewset, TransfersViewset, Job_OpeningsViewset, ProductsViewset, Co_workersViewset, CommentViewset, Be_Co_WorkerViewset, About_UsViewset, JoiningViewset, CategoryViewset, MainCategoryViewset, LegalEntitiesViewset, IndividualsViewset


router = routers.DefaultRouter()
router.register(r'tariff', TariffsViewset),
router.register(r'tender', TenderViewset),
router.register(r'transfers', TransfersViewset),
router.register(r'job_openings', Job_OpeningsViewset),
router.register(r'co_workers', Co_workersViewset),
router.register(r'products', ProductsViewset),
router.register(r'сomment', CommentViewset),
router.register(r'be_co_worker', Be_Co_WorkerViewset),
router.register(r'about_us', About_UsViewset),
router.register(r'joining', JoiningViewset),
router.register(r'category', CategoryViewset),
router.register(r'maincategory', MainCategoryViewset),
router.register(r'legalentities', LegalEntitiesViewset),
router.register(r'individuals', IndividualsViewset),

urlpatterns = [
    path('', include(router.urls)),
    # path('tariff-api/', TariffsApiListview.as_view()),
    # path('tariff-api/', TariffsViewset.as_view()),
]






