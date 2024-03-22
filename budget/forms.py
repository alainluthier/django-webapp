from django import forms
from budget.models import Category,Income,Expense

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class IncomeForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_at'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 
                'class': 'form-control'
                }
            )
        print(self.fields['created_at'])
    class Meta:
        model = Income
        fields = '__all__'

class ExpenseForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_at'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 
                'class': 'form-control'
                }
            )
        print(self.fields['created_at'])
    class Meta:
        model = Expense
        fields = '__all__'