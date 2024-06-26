from django.shortcuts import render
from .forms import DonorRegistration
from .models import DonorList

def donorregdisplay(request):
    forms = DonorRegistration()
    if request.method == 'POST':
        forms = DonorRegistration(request.POST)
        if forms.is_valid():
            forms.save()
            print(forms.errors)
            context_details ={
                'forms' : forms
            }
            return render(request, 'registrations.html', context_details)
    context = {
                'forms' : forms,
            }


    return render(request, 'register.html', context)

