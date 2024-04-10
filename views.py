from django.shortcuts import render
from .forms import UserCreateForm

def index(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'form': form}
    return render(request, 'index.html', context)
