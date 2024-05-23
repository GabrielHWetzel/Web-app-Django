from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
from .models import Form
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(first_name=first_name,
                                last_name=last_name,
                                email=email,
                                date=date,
                                occupation=occupation)
            message_body = f"New job application was submitted. {first_name}"
            email_message = EmailMessage("Form submission confirmation",
                                         message_body,
                                         to=[email])
            email_message.send()

            messages.success(request, "Form submitted successfully!")
    return render(request, "index.html")
