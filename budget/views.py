from django.shortcuts import render, redirect
from django.db.models import Sum
from budget.forms import IncomeForm,ExpenseForm
from budget.models import Income,Expense
def index(request):
    sum_expenses= Expense.objects.aggregate(Sum('amount'))
    sum_incomes= Income.objects.aggregate(Sum('amount'))
    balance = sum_incomes['amount__sum']-sum_expenses['amount__sum']
    return render(request,'index.html',context={'sum_expenses':sum_expenses,'sum_incomes':sum_incomes,'balance':balance})
def showIncomes(request):
    incomes = Income.objects.all()
    return render(request,"show_incomes.html",{'incomes':incomes})
def addIncome(request):
    if request.method=="POST":
        income = IncomeForm(request.POST)
        if income.is_valid():
            try:
                income.save()
                return redirect('/budget/incomes')
            except:
                pass
    else:
        income = IncomeForm()
    return render(request,'add_income.html',{'income':income})
def updateIncome(request,id):
    income=Income.objects.get(id=id)    
    if request.method=='POST':
        form = IncomeForm(request.POST,instance=income)
        if form.is_valid():
            form.save()
            return redirect('/budget/incomes')
    else:
        form=IncomeForm(instance=income)
    return render(request,'edit_income.html',{'income':form})
def deleteIncome(request, id):  
    income = Income.objects.get(id=id)  
    income.delete()  
    return redirect('/budget/incomes')

def showExpenses(request):
    expenses = Expense.objects.all()
    return render(request,"show_expenses.html",{'expenses':expenses})
def addExpense(request):
    if request.method=="POST":
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            try:
                expense.save()
                return redirect('/budget/expenses')
            except:
                pass
    else:
        expense = ExpenseForm()
    return render(request,'add_expense.html',{'expense':expense})
def updateExpense(request,id):
    expense=Expense.objects.get(id=id)    
    if request.method=='POST':
        form = ExpenseForm(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('/budget/expenses')
    else:
        form=ExpenseForm(instance=expense)
    return render(request,'edit_expense.html',{'expense':form})
def deleteExpense(request, id):  
    expense = Expense.objects.get(id=id)  
    expense.delete()  
    return redirect('/budget/expenses')