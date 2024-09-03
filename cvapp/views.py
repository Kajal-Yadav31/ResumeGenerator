from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from cvapp.forms import ProfileForm
from cvapp.models import Profile, ResumeTemplate
from django.views import View
from accounts.models import Account
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
from django.template import TemplateDoesNotExist

# Create your views here.


def home(request):
    return render(request, 'cvapp/home.html')


@method_decorator(login_required, name='dispatch')
class SelectTemplate(View):
    def get(self, request):
        templates = ResumeTemplate.objects.all()
        profile = Profile.objects.filter(user=request.user).first()
        return render(request, 'cvapp/select_template.html', {'templates': templates, 'profile': profile})

    def post(self, request):
        template_id = request.POST.get('template_id')
        print(f"Received Template ID: {template_id}")

        if template_id:
            selected_template = get_object_or_404(
                ResumeTemplate, id=template_id)
            profile = Profile.objects.filter(user=request.user).first()
            print(
                f"Selected Template: {selected_template.name}, Profile Exists: {bool(profile)}")

            if profile:  # Existing user
                profile.resume_template = selected_template
                profile.save()
                print(f"Template updated for Profile ID: {profile.id}")
                return redirect('viewing', id=profile.id)
            else:  # New user
                request.session['selected_template_id'] = template_id
                print("New user detected, redirecting to resume form")
                # Redirect to resume form filling page
                return redirect('accept')

        templates = ResumeTemplate.objects.all()
        print("No template selected, re-rendering select_template page")
        return render(request, 'cvapp/select_template.html', {'templates': templates})


@method_decorator(login_required, name='dispatch')
class Accept(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, 'cvapp/accept.html', {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user

            template_id = request.session.get('selected_template_id')

            if template_id:
                profile.resume_template = ResumeTemplate.objects.get(
                    id=template_id)
                del request.session['selected_template_id']
                print(
                    f"Profile will be saved with template: {profile.resume_template.name}")
            profile.save()
            return redirect('viewing', id=profile.id)

        return render(request, 'cvapp/accept.html', {'form': form})


@login_required
def resume(request, template_id):
    user_profile = get_object_or_404(Profile, pk=template_id)
    skills_list = user_profile.skills.split(',') if user_profile.skills else []

    if user_profile.resume_template and user_profile.resume_template.template_file:
        template_name = user_profile.resume_template.template_file.name
        print("the template path is :", template_name)
    else:
        template_name = 'cvapp/resume.html'

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
            template_name = 'cvapp/resume.html'
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
    # profile_id = request.user.id
    account = Account.objects.get(email__exact=request.user.email)
    Visitor = get_object_or_404(Profile, pk=id)
    print("visitor is : ", Visitor)
    print("profile_id of this user :", Visitor.id)

    if account.email == Visitor.email:

        return render(request, 'cvapp/Individual-User.html', {'Visitor': Visitor})
    else:
        return render(request, 'cvapp/unauthorized_access.html')


def update_form(request, id):
    review = Profile.objects.get(id=id)
    form = ProfileForm(request.POST or None,
                       instance=review)

    if form.is_valid():
        form.save()
        return redirect('viewing', id=id)

    return render(request, 'cvapp/accept.html', {'form': form, 'review': review})


def delete_form(request, id):
    review = Profile.objects.get(id=id)

    if request.method == 'POST':
        review.delete()
        return redirect('list')

    return render(request, 'cvapp/deletecv.html', {'review': review})
