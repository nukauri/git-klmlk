from django import forms



from .models import Account,Supplier,DocumentType

INPUT_CLASSES = 'w-full px-1 rounded-xl border bg-gray-200'

class NewAccountForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super (NewAccountForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['documentType'].queryset = DocumentType.objects.filter(accountType='GD')
        self.fields['supplier'].queryset = Supplier.objects.filter(isSupplier=True)

    class Meta:
        model = Account
        fields = ('documentGroup','documentType','documentNo','document','payType','banka','description','price','documentDate','area','accomodation','supplier','project','documentImage')
        widgets = {
            'documentGroup': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'documentType': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'documentNo': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'document': forms.Select(attrs={
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
            'documentDate': forms.DateInput(attrs={
                'class': INPUT_CLASSES,
                'type' : "date"
                
                }
            ),
            'area': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'accomodation': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'supplier': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'project': forms.Select(attrs={
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
        fields = ('documentGroup','documentType','documentNo','document','payType','banka','description','price','documentDate','area','accomodation','supplier','project','documentImage')
        widgets = {
            'documentGroup': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'documentType': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'documentNo': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'document': forms.Select(attrs={
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
            'documentDate': forms.DateInput(attrs={
                'class': INPUT_CLASSES,
                'type' : "date"
                
                }
            ),
            'area': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'accomodation': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'supplier': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'project': forms.Select(attrs={
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
        fields = ('documentGroup','documentType','documentNo','document','payType','banka','description','price','documentDate','area','accomodation','supplier','project','documentImage')
        widgets = {
            'documentGroup': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'documentType': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'documentNo': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'document': forms.Select(attrs={
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
            'documentDate': forms.DateInput(attrs={
                'class': INPUT_CLASSES,
                'type' : "date"
            }),
            'area': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'accomodation': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'supplier': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'project': forms.Select(attrs={
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
        fields = ('documentGroup','documentType','documentNo','document','payType','banka','description','price','documentDate','area','accomodation','supplier','project','documentImage')
        widgets = {
            'documentGroup': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'documentType': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'documentNo': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'document': forms.Select(attrs={
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
            'documentDate': forms.DateInput(attrs={
                'class': INPUT_CLASSES,
                'type' : "date"
            }),
            'area': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'accomodation': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'supplier': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'project': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'documentImage': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }