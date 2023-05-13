from django.core.mail import EmailMultiAlternatives 
from django.conf import settings
from celery import shared_task
from core.models import Subscription
from random import choices
@shared_task
def send_mail_to_Contact():
    email_list = Subscription.objects.all().values_list('email',flat=True)
    mail_text = f"Hello dear User, <br> A new blog has been uploaded to the site. Let's check it out! <br> Thanks, <br> <h1>Abstract</h1>"
    msg = EmailMultiAlternatives(subject='Test subject', body=mail_text, from_email=settings.EMAIL_HOST_USER, to=email_list, )
    msg.attach_alternative(mail_text, "text/html")
    msg.send()
    
    return "Mails sent successfully"

@shared_task
def send_welcome_mail(email , username):
    email_list = [email]
    mail_text = f"Hello dear {username}, <br> Welcome to our site! <br> It's a pleasure to see you among us. <br> <h1>Abstract</h1>"
    msg = EmailMultiAlternatives(subject='Test subject', body=mail_text, from_email=settings.EMAIL_HOST_USER, to=email_list, )
    msg.attach_alternative(mail_text, "text/html")
    msg.send()
    
    return "Mails sent successfully"



    
