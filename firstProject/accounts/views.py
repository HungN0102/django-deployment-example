from django.shortcuts import render
from .forms import NewUserForm
# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def customer_create_view(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error Form Invalid')

    dict_ = {
        'form': form
    }
    return render(request, 'accounts/create_account.html', context=dict_)