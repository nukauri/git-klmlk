from django import forms



from .models import Account,Supplier,DocumentType,Debit

INPUT_CLASSES = 'w-full px-1 rounded-xl border bg-gray-200'

class NewAccountForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super (NewAccountForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['documentType'].queryset = DocumentType.objects.filter(accountType='GD')
        self.fields['supplier'].queryset = Supplier.objects.filter(isSupplier=True)

    class Meta:
        model = Account
        fields = ('documentType','payType','banka','description','price','currencyUnit','documentDate','area','supplier','documentImage')
        widgets = {
            'documentType': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'payType': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'banka': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'currencyUnit': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'documentDate': forms.DateInput(attrs={
                'class': INPUT_CLASSES,
                'type' : "date"
                
                }
            ),
            'area': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'supplier': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'documentImage': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
    
class NewGelirAccountForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super (NewGelirAccountForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['documentType'].queryset = DocumentType.objects.filter(accountType='GL')
        self.fields['supplier'].queryset = Supplier.objects.filter(isCustomer=True)

    class Meta:
        model = Account
        fields = ('documentType','payType','banka','description','price','currencyUnit','documentDate','area','supplier','documentImage')
        widgets = {
            'documentType': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'payType': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'banka': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'currencyUnit': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'documentDate': forms.DateInput(attrs={
                'class': INPUT_CLASSES,
                'type' : "date"
                
                }
            ),
            'area': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'supplier': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'documentImage': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditAccountForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super (EditAccountForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['documentType'].queryset = DocumentType.objects.filter(accountType='GD')
        self.fields['supplier'].queryset = Supplier.objects.filter(isSupplier=True)

    class Meta:
        model = Account
        fields = ('documentType','payType','banka','description','price','currencyUnit','documentDate','area','supplier','documentImage')
        widgets = {
            'documentType': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'payType': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'banka': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'currencyUnit': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'documentDate': forms.DateInput(attrs={
                'class': INPUT_CLASSES,
                'type' : "date"
            }),
            'area': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'supplier': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'documentImage': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditGelirAccountForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super (EditGelirAccountForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['documentType'].queryset = DocumentType.objects.filter(accountType='GL')
        self.fields['supplier'].queryset = Supplier.objects.filter(isCustomer=True)

    class Meta:
        model = Account
        fields = ('documentType','payType','banka','description','price','currencyUnit','documentDate','area','supplier','documentImage')
        widgets = {
            'documentType': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'payType': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'banka': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'currencyUnit': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'documentDate': forms.DateInput(attrs={
                'class': INPUT_CLASSES,
                'type' : "date"
            }),
            'area': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'supplier': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'documentImage': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class NewDebitForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super (NewDebitForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['supplier'].queryset = Supplier.objects.filter(isSupplier=True)

    class Meta:
        model = Debit
        fields = ('supplier','invoiceDate','invoicePrice','description','paymentTerm','area')
        widgets = {
            'supplier': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'paymentTerm': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'invoicePrice': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'invoiceDate': forms.DateInput(attrs={
                'class': INPUT_CLASSES,
                'type' : "date"
                
                }
            ),
            'area': forms.Select(attrs={
                'class': INPUT_CLASSES
            })

        }

class EditDebitForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super (NewDebitForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['supplier'].queryset = Supplier.objects.filter(isSupplier=True)

    class Meta:
        model = Debit
        fields = ('supplier','invoiceDate','invoicePrice','description','paymentTerm','area')
        widgets = {
            'supplier': forms.Select(attrs={
                'class': INPUT_CLASSES
                
            }),
            'paymentTerm': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'invoicePrice': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'invoiceDate': forms.DateInput(attrs={
                'class': INPUT_CLASSES,
                'type' : "date"
                
                }
            ),
            'area': forms.Select(attrs={
                'class': INPUT_CLASSES
            })

        }