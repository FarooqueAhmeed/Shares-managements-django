from django import forms
from .models import Shares

class SharesForm(forms.ModelForm):
    class Meta:
        model = Shares
        fields = ['name','ticker','buy_price','number_of_shares']




'''  
class EditSharesForm(forms.ModelForm):
    class Meta:
        model = Shares
        fields = ('name','ticker','buy_price','number_of_shares')
        
'''