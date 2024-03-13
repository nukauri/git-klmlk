from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import logout

# Create your views here.

from account.models import Supplier,DocumentType,Project,Account


from .forms import SignupForm
from account.filters import AccountFilter

def index(request):
    accountlists=Account.objects.all()
    account_filter = AccountFilter(request.GET,queryset=Account.objects.all())

    paginator = Paginator(account_filter.qs,5)
    page_number = request.GET.get("page")
    accounts=paginator.get_page(page_number)
    
    context = {
        'form':account_filter.form,
        'accounts':accounts

    }


    return render(request,'core/index.html', context)

def about(request):
    return render(request, 'core/about.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def logout_view(request):
    logout(request)
    return redirect('/login/')

