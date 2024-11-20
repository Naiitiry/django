from django.forms import ModelForm
from .models import Employees

class EmployeeForm(ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'
        # Si quiero agregar otros campos
        # extra_fields = ['Salary']
        # Si quiero excluir 1 o más campos
        # exclude = ('email',)