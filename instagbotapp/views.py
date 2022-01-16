from django.shortcuts import render
from django.core.mail import send_mail
from .bot import instag_bot

def search_user(request):
    dict_context={}
    
    if request.method == "POST":
        try:
            excel=request.FILES["UploadedExcelFile"]
            context_userlist=instag_bot.get_users_by_list(excel)
            dict_context.update({"userdata_list":context_userlist})
        except:
            dict_context.update({"userdata_list":False})

    
    elif "username" in request.GET:
        try:
            context_userdata=instag_bot.get_username_data(request.GET.get("username"))
            dict_context.update({"userdata":context_userdata})
        except:
            dict_context.update({"userdata":False})

    
    return render(request, "instagbotapp/search_interface.html", dict_context)





def help(request):
    return render(request, "instagbotapp/help.html")

def contact_me(request):
    
    if request.method == "POST":
        name=request.POST["contact-us__name-form"]
        lastname=request.POST["contact-us__lastname-form"]
        subject=request.POST["contact-us__subject-form"]
        email=request.POST["contact-us__email-form"]
        phonenumber=request.POST["contact-us__phonenumber-form"]
        message=request.POST["contact-us__message-form"]
        body=f"""
        Name: {name}/n
        Lastname: {lastname}/n
        Email: {email}/n
        Phone Number: {phonenumber}/n
        Message: {message}
        """
        send_mail(subject, body, "diegorpro2024@gmail.com", ["diegorpro2024@gmail.com"])
        
    return render(request, "instagbotapp/contact_me.html")