from django import forms 
from .models import Profile

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

JOB_CITY_CHOICE = [
    ('New Delhi','New Delhi'),
    ('Noida','Noida'),
    ('Gurugram','Gurugram'),
    ('Mumbai','Mumbai'),
    ('Banglore','Banglore'),
    ('Kolkata','Kolkata'),
    ('Chennai','Chennai'),
    ('Hyderabad','Hyderabad')
]

class ProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred Job Locations', choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Profile
        fields = "__all__"
        labels = {'name':'Full Name', 'dob': 'Date of Birth', 'pin': 'Pin Code', 'phone': 'Contact No', 'email':'Email ID',
        'profile_image': 'Profile Image', 'certificate': 'Document', 'summary': 'About Yourself', 'degree': 'Degree', 'school':'School', 'university': 'University', 'previous_work': 'Previous Work', 'skills': 'Skills','city':'City', 'locality': 'Locality','state': 'State'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'summary':forms.Textarea(attrs={'class':'form-control'}),
            'degree':forms.TextInput(attrs={'class':'form-control'}),
            'school':forms.TextInput(attrs={'class':'form-control'}),
            'university':forms.Textarea(attrs={'class':'form-control'}),
            'previous_work':forms.Textarea(attrs={'class':'form-control'}),
            'skills':forms.Textarea(attrs={'class':'form-control'}),

        }

