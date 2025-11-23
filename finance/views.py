from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Sum
from .models import Income, Expense, Category
from .serializers import IncomeSerializer, ExpenseSerializer, CategorySerializer

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@api_view(['GET'])
def monthly_summary(request):
    income_total = Income.objects.aggregate(total=Sum('amount'))['total'] or 0
    expense_total = Expense.objects.aggregate(total=Sum('amount'))['total'] or 0

    summary = {
        "income": income_total,
        "expenses": expense_total,
        "balance": income_total - expense_total
    }
    return Response(summary)
