from django.shortcuts import render
from .forms import ReqForm

def index(request):
    if request.method == 'POST':
        form = ReqForm(request.POST)
        if form.is_valid():
            ReqForm.save()
    else:
        ReqForm()
    return render(request, 'map/index.html', {'form': form})