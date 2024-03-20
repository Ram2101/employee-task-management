from django import forms

class PaymentForm(forms.Form):
    amount = forms.DecimalField(label='Amount', required=True)
    currency = forms.CharField(label='Currency', initial='INR', required=True)
    razorpay_payment_id = forms.CharField(widget=forms.HiddenInput())