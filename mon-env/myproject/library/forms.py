from django import forms
from .models import Loan

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['borrower_full_name', 'borrower_email', 'library_card_number']