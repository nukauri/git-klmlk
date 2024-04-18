from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewAccountForm,EditAccountForm,EditGelirAccountForm,NewGelirAccountForm
from .models import Account

from account.filters import AccountFilter

# Create your views here.
from account.api.serializers import AccountSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

class AccountListAPIView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AccountFilter

def detail(request,pk):
    account = get_object_or_404(Account,pk=pk)

    return render(request, 'account/detail.html',{'account':account})

def detailgl(request,pk):
    account = get_object_or_404(Account,pk=pk)

    return render(request, 'account/detailgl.html',{'account':account})

@login_required
def new(request):
    if request.method == 'POST':
        form = NewAccountForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('account:detail', pk=item.id)
    else:
        form = NewAccountForm()

    return render(request, 'account/form.html', {
        'form': form,
        'title': 'Yeni Gider Girişi',
    })

@login_required
def newGelir(request):
    if request.method == 'POST':
        form = NewGelirAccountForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('account:detailgl', pk=item.id)
    else:
        form = NewGelirAccountForm()

    return render(request, 'account/form.html', {
        'form': form,
        'title': 'Yeni Gelir Girişi',
    })

@login_required
def edit(request, pk):
    account = get_object_or_404(Account, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditAccountForm(request.POST, request.FILES, instance=account)

        if form.is_valid():
            form.save()

            return redirect('account:detail', pk=account.id)
    else:
        form = EditAccountForm(instance=account)

    return render(request, 'account/form.html', {
        'form': form,
        'title': 'Gider Güncelleme',
    })

def editGelir(request, pk):
    account = get_object_or_404(Account, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditGelirAccountForm(request.POST, request.FILES, instance=account)

        if form.is_valid():
            form.save()

            return redirect('account:detailgl', pk=account.id)
    else:
        form = EditGelirAccountForm(instance=account)

    return render(request, 'account/form.html', {
        'form': form,
        'title': 'Gelir Güncelleme',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Account, pk=pk, created_by=request.user)
    item.delete()

    return redirect('core:index')
