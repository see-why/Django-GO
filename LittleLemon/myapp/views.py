from django.shortcuts import render
from django.http import JsonResponse

from myapp.forms import MenuForm
from myapp.models import Menu

# Create your views here.
def ratings(request):
    pass

def menu(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            item_name = cd['item_name']
            category = cd['category']
            description = cd['description']
            mf = Menu(item_name=item_name, category=category, description=description)
            mf.save()
            return JsonResponse({'message': 'success'})
    
    return render(request, 'menu.html', {'form': MenuForm()})