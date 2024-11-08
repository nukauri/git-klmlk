from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import logout
from django.http import HttpResponse

# Create your views here.

from account.models import Supplier,DocumentType,Project,Account
from account.resourcess import AccountResource


from .forms import SignupForm
from account.filters import AccountFilter

@login_required
def index(request):
    accountlists=Account.objects.filter(documentType__accountType="Gelir")
    account_filter = AccountFilter(request.GET,queryset=Account.objects.filter(documentType__accountType="GL").order_by("-documentDate"))

    paginator = Paginator(account_filter.qs,100)
    page_number = request.GET.get("page")
    accounts=paginator.get_page(page_number)

    accountlists2=Account.objects.all()
    account_filter2 = AccountFilter(request.GET,queryset=Account.objects.filter(documentType__accountType="GD").order_by("-documentDate"))

    paginator2 = Paginator(account_filter2.qs,100)
    page_number2 = request.GET.get("page")
    accounts2=paginator2.get_page(page_number2)

    
    sumPrice1 = 0
    for obj in account_filter.qs:
        sumPrice1 = sumPrice1 + obj.price

    sumPrice2 = 0
    for obj in account_filter2.qs:
        sumPrice2 = sumPrice2 + obj.price

    sumFark = sumPrice1 - sumPrice2

    context = {
        'form':account_filter.form,
        'accounts':accounts,
        'accounts2':accounts2,
        'sumPrice1':sumPrice1,
        'sumPrice2':sumPrice2,
        'sumFark':sumFark
       

    }


    return render(request,'core/index.html', context)


@login_required
def list(request):
    accountlists=Account.objects.filter(documentType__accountType="Gelir")
    account_filter = AccountFilter(request.GET,queryset=Account.objects.filter(documentType__accountType="GL").order_by("-documentDate"))

    accountlists2=Account.objects.all()
    account_filter2 = AccountFilter(request.GET,queryset=Account.objects.filter(documentType__accountType="GD").order_by("-documentDate"))


    
    sumPrice1 = 0
    for obj in account_filter.qs:
        sumPrice1 = sumPrice1 + obj.price

    sumPrice2 = 0
    for obj in account_filter2.qs:
        sumPrice2 = sumPrice2 + obj.price

    sumFark = sumPrice1 - sumPrice2

    context = {
        'form':account_filter.form,
        'accounts':account_filter.qs,
        'accounts2':account_filter2.qs,
        'sumPrice1':sumPrice1,
        'sumPrice2':sumPrice2,
        'sumFark':sumFark
       

    }


    return render(request,'core/list.html', context)

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

@login_required
def exportGL(request):

    if request.htmx:
        return HttpResponse(headers={'HX-Redirect':request.get_full_path()})
    
    account_filter = AccountFilter(
        request.GET,
        queryset=Account.objects.filter(documentType__accountType="GL").order_by("-documentDate")
    )

    datagl=AccountResource().export(account_filter.qs)
    response=HttpResponse(datagl.csv)
    response['Content-Disposition'] = 'attachment; filename="gelirler.csv"'
    return response

@login_required
def exportGD(request):

    if request.htmx:
        return HttpResponse(headers={'HX-Redirect':request.get_full_path()})
    
    account_filter = AccountFilter(
        request.GET,
        queryset=Account.objects.filter(documentType__accountType="GD").order_by("-documentDate")
    )

    datagd=AccountResource().export(account_filter.qs)
    response=HttpResponse(datagd.csv)
    response['Content-Disposition'] = 'attachment; filename="giderler.csv"'
    return response
