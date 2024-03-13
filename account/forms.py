from django import forms



from .models import Account

INPUT_CLASSES = 'w-full px-1 rounded-xl border bg-gray-200'

class NewAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('documentGroup','documentType','documentNo','description','price','documentDate','area','accomodation','supplier','project','documentImage')
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
            'description': forms.Textarea(attrs={
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
    class Meta:
        model = Account
        fields = ('documentGroup','documentType','documentNo','description','price','documentDate','area','accomodation','supplier','project','documentImage')
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
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'documentDate': forms.DateInput(attrs={
                'class': INPUT_CLASSES
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