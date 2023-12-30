from django.conf import settings
from django.core.mail import send_mail

def send_email_to_users():
    subject="testing subject"
    message="test massage"
    from_email=settings.EMAIL_HOST_USER
    recipient_list=["abc@gmail.com"]
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False
        )