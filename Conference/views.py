from django.shortcuts import render,get_object_or_404,redirect
from django.core.mail import send_mail
from .forms import RegistrationForm
from .models import Cityy,Categories,Registrationform


# Create your views here.

def home(request):

    cities = Cityy.objects.all()
    programs = Categories.objects.all()
   
    # sent = False

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            # subject = f"{cd['Firstname']} Participant Registration For the IMPACT conference"
            # message = f"Thank you for registering for the IMPACT 2021 conference that will be held UCU main campus.Join us as we learn from developers and researchers around the world."
            # send_mail(subject, message, 'ronaldrani72@gmail.com',[cd['Email']])

            # sent = True

            return redirect('/')

    else:
        form = RegistrationForm()
    return render(request, 'Conference/home.html',{'form':form,'cities':cities,'programs':programs})

    
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            subject = f"{cd['name']} Participant Registration For the IMPACT conference"
            message = f"Thank you for registering for the IMPACT 2021 conference that will be held UCU main campus.Join us as we learn from developers and researchers around the world."
            send_mail(subject, message, 'ronaldrani72@gmail.com',[cd['email']])

            sent = True

            return redirect('/')

    else:
        form = RegistrationForm()
    return render(request, 'Conference/register.html',{'form':form,})
