from django.http import HttpResponse

from myapp.task import send_email_fun
from ProjectCelery import settings

def send_email(request):
    send_email_fun.delay("your_subject", "your_message", settings.EMAIL_HOST_USER, "xefonzero2101@gmail.com")
    return HttpResponse("Sent Email Successfully...Check your mail please")
