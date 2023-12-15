from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ('user',)
        labels = {'first_name': 'First Name',  'surname': 'Surname', 'profession': 'Job Title', 'phone': 'Contact No', 'email': 'Email ID', 'locality': 'Locality', 'city': 'City', 'state': 'State', 'Pin_code': 'Pin Code', 'linkedin_link': 'LinkedIn', 'Github_link': 'GitHub',  'About': 'About Yourself', 'degree': 'Degree',
                  'school_name': 'School Name', 'school_location': 'School Location', 'College': 'College Name', 'project': 'List of Projects', 'university': 'University', 'work_experience': 'Experience', 'skills': 'Skills', 'Interest': 'Your Interests', 'profile_image': 'Profile Image', 'certificate': 'Certificates'}
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Last Name'}),
            'profession': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg., Software Developer'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email Id'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'eg., 1234567890'}),
            'locality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg., Rohini'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg., South delhi'}),
            'state': forms.Select(attrs={'class': 'form-control', 'placeholder': 'eg., New Delhi'}),
            'Pin_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'eg., 123456'}),
            'linkedin_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'eg., https://someone32'}),
            'Github_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'eg., Someone32'}),
            'About': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Brief Description about yourself'}),
            'school_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your School name'}),
            'scholl_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg., Rohini,South delhi, New delhi'}),
            'College': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your College name'}),
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg., B-tech'}),
            'university': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg., AKTU'}),
            'project': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your projects'}),
            'Work_experience': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your work enperience'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the skills that you have'}),
            'Interest': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your Interest'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
            'certificate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Cerificaitons that you have done.'}),
        }
