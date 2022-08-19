from django.shortcuts import redirect, render
from .forms import busForm
from .models import busService

# Create your views here.
def form(request, id=0):
    if request.method=='GET':
        if id==0:
            data=busForm
        else:
            bus=busService.objects.get(pk=id)
            data=busForm(instance=bus)
    else:
        if id==0:
            data=busForm(request.POST)
        else:
            bus=busService.objects.get(pk=id)
            data=busForm(request.POST, instance=bus)
        if data.is_valid():
            data.save()
            return redirect('list')
    return render(request, 'form.html', {'form':data})

def showTicket(request):
    show_data=busService.objects.all()
    return render(request, 'list.html', {'data':show_data})
    data=busService.objects.get(pk=id)
    data.delete()
    return redirect('list')