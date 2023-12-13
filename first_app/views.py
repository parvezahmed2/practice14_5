from django.shortcuts import render
from . forms import ApiForm
from first_app.forms import PracticeForm

# Create your views here.
# ----------------- Model form -------------------------------
# def home(request):
#     if request.method == 'POST':
#         form = PracticeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print(form.cleaned_data)

#     else:
#         form = PracticeForm()    
#     return render(request, 'home.html', {'form': form})


def home(request):
    if request.method == 'POST':
        form =  ApiForm(request.POST, request.FILES)
        if form.is_valid():
             
            print(form.cleaned_data)        
    else:
        form=  ApiForm()    
    return render(request, 'home.html', {'form': form} )
