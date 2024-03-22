from django.db import models

class Category(models.Model):
    id=models.AutoField(primary_key=True)
    category=models.CharField(max_length=200)
    class Meta:
        db_table="category"
class Income(models.Model):
    id=models.AutoField(primary_key=True)
    amount=models.FloatField()
    created_at=models.DateField(null=True,blank=True)
    SOURCE_INCOME = (
        ('s', 'Salary'),
        ('o', 'Other')
    )
    source=models.CharField(max_length=1,choices=SOURCE_INCOME,blank=True,default='s',help_text="Source type")
    class Meta:
        db_table="income"
class Expense(models.Model):
    id=models.AutoField(primary_key=True)
    amount=models.FloatField()
    created_at=models.DateField(null=True,blank=True)
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    description=models.CharField(max_length=300)
    class Meta:
        db_table="expense"
