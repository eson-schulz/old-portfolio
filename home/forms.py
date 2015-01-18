from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control',
																		'placeholder':'Name',
																		'id':'name'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',
															'placeholder':'Email Address',
															'id':'email'}))
	message = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'rows':'5',
																			'class':'form-control',
																			'placeholder':'Message',
																			'id':'message'}))