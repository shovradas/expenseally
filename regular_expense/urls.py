from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-expense', views.add_expense, name='add-expense'),
    path('manage-expense', views.manage_expense, name='manage-expense'),
    path('expense-settings', views.expense_settings, name='expense-settings'),
]