from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewAccountForm,EditAccountForm,EditGelirAccountForm,NewGelirAccountForm,NewDebitForm,EditDebitForm,EditCreditForm,NewCreditForm,ReportForm
from .models import Account,Debit,Credit

from account.filters import AccountFilter
from django.db.models import Sum,Count
from django.db.models.functions import ExtractDay,ExtractMonth,ExtractWeekDay,ExtractYear,ExtractWeek
#from datetime import date
import datetime
import pandas as pd
from django.db.models import F

import plotly.express as px
import plotly.graph_objects as go

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

@login_required
def deleteDebit(request, pk):
    item = get_object_or_404(Debit, pk=pk)
    item.delete()

    return redirect('account:debit')

@login_required
def newDebit(request):
    debitlist = Debit.objects.all()
    total = Debit.objects.all().aggregate(total=Sum('invoicePrice'))['total']
    if request.method == 'POST':
        form = NewDebitForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            
    else:
        form = NewDebitForm()

    return render(request, 'core/debit.html', {
        'form': form,
        'title': 'Yeni Borç Girişi',
        'debits':debitlist,
        'total':total
    })

@login_required
def editDebit(request, pk):
    debitlist = Debit.objects.all()
    debit = get_object_or_404(Debit, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditDebitForm(request.POST, request.FILES, instance=debit)

        if form.is_valid():
            form.save()

            return redirect('account:debitdetail', pk=debit.id)
    else:
        form = EditDebitForm(instance=debit)

    return render(request, 'core/debit.html', {
        'form': form,
        'title': 'Borç Güncelleme',
        'debits':'debitlist'
    })

@login_required
def deleteCredit(request, pk):
    item = get_object_or_404(Credit, pk=pk)
    item.delete()

    return redirect('account:credit')

@login_required
def newCredit(request):
    creditlist = Credit.objects.all()
    total = Credit.objects.all().aggregate(total=Sum('invoicePrice'))['total']
    if request.method == 'POST':
        form = NewCreditForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            
    else:
        form = NewCreditForm()

    return render(request, 'core/credit.html', {
        'form': form,
        'title': 'Yeni Alacak Girişi',
        'credits':creditlist,
        'total':total
    })

@login_required
def editCredit(request, pk):
    creditlist = Credit.objects.all()
    credit = get_object_or_404(Credit, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditCreditForm(request.POST, request.FILES, instance=credit)

        if form.is_valid():
            form.save()

            return redirect('account:creditdetail', pk=credit.id)
    else:
        form = EditCreditForm(instance=credit)

    return render(request, 'core/credit.html', {
        'form': form,
        'title': 'Alacak Güncelleme',
        'credits':'creditlist'
    })

@login_required
def report(request):
    startdate = 0
    enddate = 0
    birim = ''
    if request.method == 'POST':
        if request.POST.get('startDate'):
            startdate = datetime.datetime.strptime(request.POST.get('startDate'), '%Y-%m-%d').date()
            if request.POST.get('endDate'):
                enddate = datetime.datetime.strptime(request.POST.get('endDate'), '%Y-%m-%d').date()
            else:
                enddate = datetime.datetime.strptime(request.POST.get('startDate'), '%Y-%m-%d').date()  
        else:
            startdate = datetime.date.today()
            enddate = datetime.date.today()
        birim = request.POST.get('birim')
    else:
        startdate = datetime.date.today()
        enddate = datetime.date.today()

    dailydate = startdate + datetime.timedelta(days=-7)
    weeklydate = startdate + datetime.timedelta(days=-2*30)
    monthlydate = startdate + datetime.timedelta(days=-6*30)

    if request.POST.get('birim'):
        qs = Account.objects.filter(documentDate__gte=startdate,documentDate__lte=enddate,area=birim,documentType__accountType="GD").values('documentDate','price',birim=F('area__name'))
        qs0 = Account.objects.filter(documentDate__gte=startdate,documentDate__lte=enddate,area=birim,documentType__accountType="GD").values('documentDate','price',birim=F('area__name'),ÖDEMETİPİ=F('payType__name'))

        qs1 = (Account.objects.filter(documentDate__gte=dailydate,documentDate__lte=startdate,area=birim).annotate(year=ExtractYear('documentDate')).annotate(week=ExtractWeekDay('documentDate')).values('year', 'week',tarih=F('documentDate'),tip=F('documentType__accountType')).annotate(topprice=Sum('price')))

        qs2 = (Account.objects.filter(documentDate__gte=weeklydate,documentDate__lte=startdate,area=birim).annotate(year=ExtractYear('documentDate')).annotate(week=ExtractWeek('documentDate')).values('year', 'week',tip=F('documentType__accountType')).annotate(topprice=Sum('price')))

        qs3 = (Account.objects.filter(documentDate__gte=monthlydate,documentDate__lte=startdate,area=birim).annotate(year=ExtractYear('documentDate')).annotate(month=ExtractMonth('documentDate')).values('year', 'month',tip=F('documentType__accountType')).annotate(topprice=Sum('price')))

    else:
        qs = Account.objects.filter(documentDate__gte=startdate,documentDate__lte=enddate,documentType__accountType="GD").values('documentDate','price',birim=F('area__name'))
        qs0 = Account.objects.filter(documentDate__gte=startdate,documentDate__lte=enddate,documentType__accountType="GD").values('documentDate','price',birim=F('area__name'),ÖDEMETİPİ=F('payType__name'))

        qs1 = (Account.objects.filter(documentDate__gte=dailydate,documentDate__lte=startdate).annotate(year=ExtractYear('documentDate')).annotate(week=ExtractWeekDay('documentDate')).values('year', 'week',tarih=F('documentDate'),tip=F('documentType__accountType')).annotate(topprice=Sum('price')))

        qs2 = (Account.objects.filter(documentDate__gte=weeklydate,documentDate__lte=startdate).annotate(year=ExtractYear('documentDate')).annotate(week=ExtractWeek('documentDate')).values('year', 'week',tip=F('documentType__accountType')).annotate(topprice=Sum('price')))

        qs3 = (Account.objects.filter(documentDate__gte=monthlydate,documentDate__lte=startdate).annotate(year=ExtractYear('documentDate')).annotate(month=ExtractMonth('documentDate')).values('year', 'month',tip=F('documentType__accountType')).annotate(topprice=Sum('price')))
        
        qs4 = (Account.objects.filter(documentDate__gte=startdate,documentDate__lte=enddate).values(birim=F('area__name'), tip=F('documentType__accountType')).annotate(topprice=Sum('price')))

    config = {'scrollZoom': True,'responsive':True}
    if qs1:
        df1 = pd.DataFrame(list(qs1))
        fig1 = px.bar(df1, x="tarih", y="topprice",  title='Son Yedi Gün'+'( '+dailydate.strftime('%d/%m/%Y')+'-'+startdate.strftime('%d/%m/%Y')+') gelir/gider tablosu',
             color='tip', barmode='group',
             text_auto=True,
             labels={ # replaces default labels by column name
                "tip": "Tip",  "tarih": "Tarih", "topprice": "Tutar"
            },
            color_discrete_sequence=[ 'red','green'],
             height=400)
        chart1=fig1.to_html(config=config)
    else:
        chart1=''
    
    if qs2:
        df2 = pd.DataFrame(list(qs2))
        fig2 = px.bar(df2, x="week", y="topprice",  title='Son Sekiz Hafta'+'( '+weeklydate.strftime('%d/%m/%Y')+'-'+startdate.strftime('%d/%m/%Y')+') gelir/gider grafiği',
             color='tip', barmode='group',
             labels={ # replaces default labels by column name
                "tip": "Tip",  "week": "hafta", "topprice": "Tutar"
            },
            text_auto=True,
            color_discrete_sequence=[ 'red','green'],
             height=400)
        chart2=fig2.to_html(config=config)
    else:
        chart2=''
    
    if qs3:
        df3 = pd.DataFrame(list(qs3))
        fig3 = px.bar(df3, x="month", y="topprice", title='Son Altı Ay'+'( '+monthlydate.strftime('%d/%m/%Y')+'-'+startdate.strftime('%d/%m/%Y')+') gelir/gider grafiği',
             color='tip', barmode='group',
             labels={ # replaces default labels by column name
                "tip": "Tip",  "month": "ay", "topprice": "Tutar"
            },
            text_auto=True,
            color_discrete_sequence=[ 'red','green'],
             height=400)
        chart3=fig3.to_html(config=config)
    else:
        chart3=''

    if qs4:
        df4 = pd.DataFrame(list(qs4))
        fig4 = px.bar(df4, x="birim", y="topprice", title='( '+startdate.strftime('%d/%m/%Y')+'-'+enddate.strftime('%d/%m/%Y')+')'+' tarihleri arası gelir/gider grafiği',
             color='tip', barmode='group',
             labels={ # replaces default labels by column name
                "tip": "Tip",  "birim": "Birim", "topprice": "Tutar"
            },
            text_auto=True,
            color_discrete_sequence=[ 'red','green'],
             height=400)
        chart4=fig4.to_html(config=config)
    else:
        chart4=''

    if qs:
        df = pd.DataFrame(list(qs))
        
        df['idx']=df.groupby('birim').cumcount()
        pivot = df.pivot(index='idx', columns='birim', values='price').fillna('')

        x1,y1 = pivot.shape
        #fig0 = go.Figure(data=[go.Table(header=dict(values=list(pivot.columns),fill_color='paleturquoise',align='left'),
        #        cells=dict(values=[pivot[col] for col in pivot.columns],
        #       fill_color='lavender',
        #       align='right'))
        #        ])

        #chart0 = fig0.to_html(config=config)

        dfx = pd.DataFrame(list(qs0))
        
        pivotz = dfx.pivot_table(index='ÖDEMETİPİ', columns='birim', values='price',aggfunc='sum').fillna('')
        pivotx =pivotz.reset_index()
        pivotxx = pd.concat([pivot,pivotx]).fillna('')
        x2,y2 = pivotxx.shape


    
    

       

        figx = go.Figure(data=[go.Table(header=dict(values=list(pivotxx.columns),fill_color='paleturquoise',align='left'),
                cells=dict(values=[pivotxx[col] for col in pivotxx.columns],
               fill_color='lightgrey',
                align='right'))
                ])
        figx.update_layout(title_text='günlük gelir gider çizelgesi')
        figx.update_layout({'margin':{'t':50,'l':50}})
        chartx = figx.to_html(config=config)

        tablo1 = pivot.to_html(index=False,escape=False,border=1,classes=['table-auto','border-collapse', 'border', 'border-slate-400','bg-gray-200'])
    else:
        tablo1=''
        chart0=''
        chartx=''



    form = ReportForm(request.POST)



    return render(request, 'core/report.html', {
        'form': form,
        'startdate': startdate,
        'enddate': enddate,
        'dailydate':dailydate,
        'weeklydate':weeklydate,
        'monthlydate': monthlydate,
        'birim' : birim,
        'tablo1' : tablo1,
        'chart1' : chart1,
        'chart2' : chart2,
        'chart3' : chart3,
        'chart4' : chart4,
        'chartx' : chartx,
        'accounts': qs1
    })