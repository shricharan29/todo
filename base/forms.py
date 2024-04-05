from django.forms import ModelForm, DateInput, TimeInput
from .models import Todo

class DatePicker(DateInput):
    input_type = 'date'

class TimePicker(TimeInput):
    input_type = 'time'

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        feilds = '__all__'
        exclude = ['done','user']
        widgets = {
            'due_date': DatePicker(),
            'due_time': TimePicker(),
        }