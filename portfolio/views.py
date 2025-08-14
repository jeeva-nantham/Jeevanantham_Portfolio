from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings

def home_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            full_message = f"Message from {name} ({email}):\n\n{message}"

            send_mail(
                subject="New Contact Form Submission",
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],  # send to yourself
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, './portfolio/index.html', {'form': form})


