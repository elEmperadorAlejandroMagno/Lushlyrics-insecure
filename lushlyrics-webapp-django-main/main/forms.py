from django import forms

class User_login_form(forms.Form):
  user_email = forms.CharField(label='Email:', max_length=50)
  username = forms.CharField(label='Username:', max_length=20)
  user_password = forms.CharField(label='Password:', max_length=20)
  confirm_password = forms.CharField(label='Confirm Password:', max_length=20)


class Password_reset_email_form(forms.Form):
  user_email = forms.CharField(label='Email:', max_length=50)

class Password_reset_form(forms.Form):
  new_password = forms.CharField(label='New Password:', max_length=20)
  confirm_new_password = forms.CharField(label='Confirm Password:', max_length=20)

