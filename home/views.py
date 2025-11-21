from django.shortcuts import render

from django.core.mail import send_mail

# Create your views here.

def index(request):
    success = False

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject="New Contact Form Message",
            message=full_message,
            from_email="gsdevadath611@gmail.com",
            recipient_list=["gsdevadath611@gmail.com"],
            fail_silently=False,
        )

        success = True  # <-- VERY IMPORTANT

    return render(request, "home/index.html", {"success": success})
