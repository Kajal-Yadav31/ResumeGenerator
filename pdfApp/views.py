from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Profile
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
                return HttpResponseRedirect('/home/')
            return render(request, 'pdfApp/accept.html',{'form':form})


def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdfApp/resume.html')
    html = template.render({'user_profile':user_profile})
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


# class UserDetailView(View):

def UserDetail(request, id):
    Visitor = Profile.objects.get(pk=id)

    return render(request, 'pdfApp/Individual-User.html', {'Visitor': Visitor})

