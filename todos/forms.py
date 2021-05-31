from django import forms
from django.forms import ModelForm
from .models import Todos


class TodoForm(ModelForm):
    class Meta:
        model = Todos
        fields = "__all__"
        # widgets = {
        #     'task': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Enter the Task"),
        #     'date': forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control'}), input_formats=['%d/%m/%y'],
        #                   label="Enter The Date")
        #     # 'status': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='status')
        # }

# class TodosForm(forms.Form):
#     task=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Enter the Task")
#     date=forms.DateField(widget=forms.TextInput(attrs={'class':'form-control'}),input_formats=['%d/%m/%y'],label="Enter The Date")
#     statuses={
#         ("completed",completed),
#         ("Incomplete","Incomplete")
#     }
#     status=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='status',choices=statuses)
#
#     def clean(self):
#         cleaned_data = super().clean()
