"""
URL configuration for personalbudget project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from budget import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('budget', views.index),
    path('budget/incomes',views.showIncomes),
    path('budget/incomes/add',views.addIncome),
    path('budget/incomes/update/<int:id>',views.updateIncome),
    path('budget/incomes/delete/<int:id>',views.deleteIncome),
    path('budget/expenses',views.showExpenses),
    path('budget/expenses/add',views.addExpense),
    path('budget/expenses/update/<int:id>',views.updateExpense),
    path('budget/expenses/delete/<int:id>',views.deleteExpense)
]
