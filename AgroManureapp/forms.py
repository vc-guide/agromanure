from django import forms
from .models import Order_details

'''
class orderInfo(forms.ModelForm):
  class Meta:
    model=Order_details
    fields =('Name','Address','phoneNo','pincode')

    def clean_phoneNo(self):
      phoneNo = self.cleaned_data['phoneNo']
      if not phoneNo.isdigit():
        raise forms.ValidationError('Phone number must contain only numbers')
      return phoneNo
    
    def clean_pincode(self):
      pincode=self.cleaned_data['pincode']
      if not pincode.isdigit():
        raise forms.ValidationError('Pin code must contain only numbers')
      return pincode
      ''' 
    

