from django.shortcuts import render
from datetime import datetime
from django.core.mail import send_mail
from .models import Send_messate

# Create your views here.
current_date = datetime.now()
def index(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        smg =  request.POST['comment']
        sends = Send_messate(name=name, email=email,message=smg)
        sends.save()

        
        subject = sends.name and sends.email          
        message = sends.message
        email_from = sends.email
        recipient_list = ['bijay2310tamang@gmail.com']
        send_mail(subject,message, email_from,recipient_list,fail_silently=False)

        # subject = 'bijay test email'
        # message = render_to_string('mess.html')
        # from_email = 'bijay2310tamang@gmail.com'
        # recipient_list = [student.email]
        # send_mail(subject,message,from_email,recipient_list,fail_silently=False)

    return render(request, 'index.html',{'current_date':current_date})

