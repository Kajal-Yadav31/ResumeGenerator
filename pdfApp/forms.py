from django import forms 
from .models import Profile

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

class ProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Profile
        fields = "__all__"
        labels = {'name':'Full Name', 'dob': 'Date of Birth', 'phone': 'Contact No', 'email':'Email ID','profession': 'Profession',
        'profile_image': 'Profile Image', 'certificate': 'Certificates', 'summary': 'About Yourself', 'degree': 'Degree', 'school':'School', 'university': 'University', 'previous_work': 'Work Experience', 'skills': 'Skills','city':'City', 'locality': 'Locality','state': 'State', 'linkedin_link':'Linkedin-Link', 'Interest':'Your Interests'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control'}),
            'profession':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'linked_link': forms.URLInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'summary':forms.Textarea(attrs={'class':'form-control'}),
            'degree':forms.TextInput(attrs={'class':'form-control'}),
            'school':forms.TextInput(attrs={'class':'form-control'}),
            'university':forms.Textarea(attrs={'class':'form-control'}),
            'previous_work':forms.Textarea(attrs={'class':'form-control'}),
            'skills':forms.Textarea(attrs={'class':'form-control'}),
            'Interest':forms.Textarea(attrs={'class':'form-control'}),
            'profile_image':forms.FileInput(attrs={'class':'form-control'}),
            'certificate':forms.TextInput(attrs={'class':'form-control'}),
        }

