from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from cvapp.forms import ProfileForm
from cvapp.models import Profile, ResumeTemplate
from django.views import View
from accounts.models import Account
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
from django.views import View
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
from django.template import TemplateDoesNotExist

# Create your views here.


def home(request):
    return render(request, 'cvapp/home.html')


def select_template(request):
    templates = ResumeTemplate.objects.all()
    if request.method == 'POST':
        template_id = request.POST.get('template_id')
        if template_id:
            print("the template_id is", template_id)
            request.session['selected_template_id'] = template_id
            return redirect('accept')  # Redirect to the resume form page

    return render(request, 'cvapp/select_template.html', {'templates': templates})


@method_decorator(login_required, name='dispatch')
class acceptView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, 'cvapp/accept.html', {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            template_id = request.session.get('selected_template_id')
            if template_id:
                print("template_id is:", template_id)
                profile.resume_template = ResumeTemplate.objects.get(
                    id=template_id)
                print(f"Saved Profile Template: {profile.resume_template}")
            profile.save()
            return redirect('list')

        return render(request, 'cvapp/accept.html', {'form': form})


def resume(request, template_id):
    user_profile = get_object_or_404(Profile, pk=template_id)
    skills_list = user_profile.skills.split(',') if user_profile.skills else []

    if user_profile.resume_template and user_profile.resume_template.template_file:
        template_name = user_profile.resume_template.template_file.name
        print("the template path is :", template_name)
    else:
        template_name = 'cvapp/resume.html'  # Default template

    try:
        if template_name in ['templates/resumetemplate1.html', 'templates/resumetemplate1_BKAojHd.html']:
            template_name = 'cvapp/resumetemplate1.html'
        elif template_name in ['templates/resumetemplate2.html', 'templates/resumetemplate2_wyrTToV.html']:
            template_name = 'cvapp/resumetemplate2.html'
        elif template_name == 'templates/resumetemplate3.html':
            template_name = 'cvapp/resumetemplate3.html'
        elif template_name in ['templates/resumetemplate4.html', 'templates/resumetemplate4_OtBYUll.html']:
            template_name = 'cvapp/resumetemplate4.html'
        elif template_name == 'templates/resumetemplate5.html':
            template_name = 'cvapp/resumetemplate5.html'
        else:
            template_name = 'cvapp/resume.html'  # Default template

        html = loader.render_to_string(
            template_name, {'user_profile': user_profile, 'skills_list': skills_list})
    except TemplateDoesNotExist:
        print(f"TemplateDoesNotExist error for: {template_name}")
        html = loader.render_to_string(
            'cvapp/resume.html', {'user_profile': user_profile, 'skills_list': skills_list})
    except Exception as e:
        print(f"Error rendering template: {e}")
        html = loader.render_to_string(
            'cvapp/resume.html', {'user_profile': user_profile, 'skills_list': skills_list})

    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        'no-stop-slow-scripts': '',
        'disable-external-links': '',
        'disable-internal-links': ''
    }

    pdf = pdfkit.from_string(html, False, options)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{user_profile.first_name}_resume.pdf"'

    return response


def list(request):
    UserCV = Profile.objects.all()
    return render(request, 'cvapp/list.html', {'UserCV': UserCV})


@login_required
def UserDetail(request, id):
    # account = Account.objects.get(email__exact=request.user.email)
    Visitor = get_object_or_404(Profile, pk=id)

    # if account.email == Visitor.email:

    return render(request, 'cvapp/Individual-User.html', {'Visitor': Visitor})
    # else:
    # return render(request, 'cvapp/unauthorized_access.html')


def update_form(request, id):
    review = Profile.objects.get(id=id)
    form = ProfileForm(request.POST or None,
                       instance=review)

    if form.is_valid():
        form.save()
        return redirect('accept')

    return render(request, 'cvapp/accept.html', {'form': form, 'review': review})


def delete_form(request, id):
    review = Profile.objects.get(id=id)

    if request.method == 'POST':
        review.delete()
        return redirect('list')

    return render(request, 'cvapp/deletecv.html', {'review': review})
