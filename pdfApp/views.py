from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Resume
from .forms import ProfileForm
from django.views import View
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.

class acceptView(View):
        def get(self, request):
            form = ProfileForm()
            return render(request, 'pdfApp/accept.html',{'form':form})
             
        def post(self, request):
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("accept")
            return render(request, 'pdfApp/accept.html',{'form':form})


def resume(request, resume_id):
    user_profile = Profile.objects.get(pk=resume_id) 
    template = loader.get_template('pdfApp/resume.html')
    html = template.render({'user_profile':user_profile })
    options = {
        'page-size': 'Letter',
        'encoding':"UTF-8",
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "resume.pdf"

    return response


def list(request):
    profiles = Profile.objects.all()
    return render(request,'pdfApp/list.html', {'profiles':profiles})



@login_required
def UserDetail(request, id):
    Visitor = Profile.objects.get(pk=id)

    return render(request, 'pdfApp/Individual-User.html', {'Visitor': Visitor})



def update_form(request, id):
    review = Profile.objects.get(id=id)
    form =  ProfileForm(request.POST or None, instance=review)

    if form.is_valid():
        form.save()
        return redirect('accept')
    
    return render(request, 'pdfApp/accept.html',{'form':form, 'review':review})


def delete_form(request, id):
    review = Profile.objects.get(id=id)

    if request.method == 'POST':
        review.delete()
        return redirect('list')
    
    return render(request,'pdfApp/deletecv.html', {'review': review})