from django import forms
from django.forms import Form
from organisation.models import Organisation
from sector.models import Sector


class DateInput(forms.DateInput):
    input_type = "date"


class AddOrgForm(forms.Form):
    organisation_name = forms.CharField(label="Organisation Name", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(
        attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", max_length=50,
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))

    try:
        sector = Sector.objects.all()
        sector_list = []
        for sector in sector:
            single_sector = (sector.id, sector.sector_name)
            sector_list.append(single_sector)

    except:
        sector_list = []

    sector_id = forms.ChoiceField(label="Sector", choices=sector_list, widget=forms.Select(
        attrs={"class": "form-control"}))
