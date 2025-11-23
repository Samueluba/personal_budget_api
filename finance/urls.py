from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, ExpenseViewSet, CategoryViewSet, monthly_summary

router = DefaultRouter()
router.register('income', IncomeViewSet)
router.register('expenses', ExpenseViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('summary/', monthly_summary),
]
