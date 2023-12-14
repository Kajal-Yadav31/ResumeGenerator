from django.shortcuts import render, redirect
from cvapp.forms import ProfileForm
from cvapp.models import Profile
from django.views import View

# Create your views here.


def home(request):
    return render(request, 'cvapp/home.html')


class acceptView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, 'cvapp/accept.html', {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("accept")
        return render(request, 'cvapp/accept.html', {'form': form})
