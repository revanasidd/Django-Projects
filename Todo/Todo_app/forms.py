from django.forms import ModelForm
from Todo_app.models import TodoListModel

#Creating Forms Class here becuse of its inbuit
class TodoForm(ModelForm):
    class Meta:
        model = TodoListModel
        fields  = '__all__'