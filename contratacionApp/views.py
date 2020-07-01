from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from contratacionApp.models import PrivateContract, CurrentContract
from django.template.context import RequestContext
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from datetime import datetime
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.views import View
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from decouple import config

# Create your views here.

def home(request):
    return render(request, 'home.html')

def noAutenticate(request):
    return render(request, 'pagesError401.html')


@login_required(login_url='/login/')
def profile(request):
    user = None
    try:
        user = User.objects.get(id=request.user.id)
    except:
        pass
    try:
        if not user.is_staff:
            return redirect("/noAutenticate/")
    except:
        pass
    today = datetime.today()
    countUser = User.objects.count()
    countPrivateContract = PrivateContract.objects.count()
    countCurrentContract = CurrentContract.objects.count()
    newPrivateContract = PrivateContract.objects.filter(Q(startDate__year=today.year, startDate__day=today.day)).count()
    newCurrentContract = CurrentContract.objects.filter(Q(startDate__year=today.year, startDate__day=today.day)).count()
    oldPrivateContract = PrivateContract.objects.filter(Q(endDate__year=today.year, endDate__month=today.month+1)).values('headline')
    oldCurrentContract = CurrentContract.objects.filter(Q(endDate__year=today.year, endDate__month=today.month+1)).values('headline')
    countOldPrivateContract = PrivateContract.objects.filter(Q(endDate__year=today.year, endDate__month=today.month)).count()
    countOldCurrentContract = CurrentContract.objects.filter(Q(endDate__year=today.year, endDate__month=today.month)).count()
    allOldContract = countOldCurrentContract + countOldPrivateContract
    return render_to_response('profile.html', {'user':user, 'countUser': countUser, 'countPrivateContract':countPrivateContract, 'countCurrentContract':countCurrentContract, 'newPrivateContract':newPrivateContract, 'newCurrentContract':newCurrentContract, 'countOldPrivateContract':countOldPrivateContract, 'oldPrivateContract':oldPrivateContract, 'allOldContract':allOldContract})

@login_required(login_url='/login/')
def privateContract(request):
    user = None
    try:
        user = User.objects.get(id=request.user.id)
    except:
        pass
    try:
        if not user.is_staff:
            return redirect("/noAutenticate/")
    except:
        pass
    today = datetime.today()
    allPrivateContract = PrivateContract.objects.filter(Q(startDate__year=today.year, startDate__month=today.month))
    paginator = Paginator(allPrivateContract, 50)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    try:
        allPrivateContractPage = paginator.page(page)
    except (EmptyPage, InvalidPage):
        allPrivateContractPage = paginator.page(paginator.num_pages)
    return render_to_response('privateContract.html', { 'user': user, 'username': request.user.username, 'allPrivateContract': allPrivateContract, 'allPrivateContractPage': allPrivateContractPage})

@login_required(login_url='/login/')
def currentContract(request):
    user = None
    try:
        user = User.objects.get(id=request.user.id)
    except:
        pass
    try:
        if not user.is_staff:
            return redirect("/noAutenticate/")
    except:
        pass
    today = datetime.today()
    allCurrentContract = CurrentContract.objects.filter(Q(startDate__year=today.year, startDate__month=today.month))
    paginator = Paginator(allCurrentContract, 50)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    try:
        allCurrentContractPage = paginator.page(page)
    except (EmptyPage, InvalidPage):
        allCurrentContractPage = paginator.page(paginator.num_pages)
    return render_to_response('currentContract.html', { 'user': user, 'username': request.user.username, 'allCurrentContract': allCurrentContract, 'allCurrentContractPage': allCurrentContractPage})

@login_required(login_url='/login/')
def contractsExpire(request):
    user = None
    try:
        user = User.objects.get(id=request.user.id)
    except:
        pass
    try:
        if not user.is_staff:
            return redirect("/noAutenticate/")
    except:
        pass
    today = datetime.today()
    expirePrivateContract = PrivateContract.objects.filter(Q(endDate__year=today.year, endDate__month=today.month+1))
    expireCurrentContract = CurrentContract.objects.filter(Q(endDate__year=today.year, endDate__month=today.month+1))
    expireDayPrivateContract = PrivateContract.objects.filter(Q(endDate__month=today.month, endDate__year=today.year))
    expireDayCurrentContract = CurrentContract.objects.filter(Q(endDate__month=today.month, endDate__year=today.year))
    return render_to_response('contractExpire.html', { 'user': user, 'username': request.user.username, 'expirePrivateContract': expirePrivateContract, 'expireCurrentContract': expireCurrentContract, 'expireDayPrivateContract': expireDayPrivateContract, 'expireDayCurrentContract': expireDayCurrentContract})

@login_required(login_url='/login/')
def filterContractByYear(request):
    user = None
    allCurrentContract = None
    allPrivateContract = None
    messageCurrentContract = None
    messagePrivateContract = None
    try:
        user = User.objects.get(id=request.user.id)
    except:
        pass
    try:
        if not user.is_staff:
            return redirect("/noAutenticate/")
    except:
        pass
    if request.method == 'POST':
        idTypeContract = int(request.POST['typeContract'])
        anio = request.POST['anio']
        if idTypeContract == 1:
            allCurrentContract = CurrentContract.objects.filter(startDate__year=anio)
            if not allCurrentContract :
                messageCurrentContract = 'No hay contratos por empresas en dicho año'            
        if idTypeContract == 2:
            allPrivateContract = PrivateContract.objects.filter(startDate__year=anio)
            if not allPrivateContract :
                messagePrivateContract = 'No hay contratos por cuenta propia en dicho año'
            

    return render(request, 'filterContract.html', { 'user': user, 'username': request.user.username, 'messagePrivateContract': messagePrivateContract, 'messageCurrentContract': messageCurrentContract, 'allCurrentContract': allCurrentContract, 'allPrivateContract': allPrivateContract})

class CronView(View):
    def get(self, request):
        token = request.GET.get('token')
        if token == settings.CRON_TOKEN:
            subject = 'Contratos a vencer en este mes'
            from_email = settings.EMAIL_FROM
            to = settings.CONTRACT_EXPIRATION_NOTIFICATIONS_EMAIL
            text_content = 'Estos son los contratos que vencen este mes:\nhttp://contratacion.apps.reduc.edu.cu/accounts/profile/expireContract/'
            html_content = '<body>Estos son los contratos que vencen este mes:  <a href=http://contratacion.apps.reduc.edu.cu/accounts/profile/expireContract/>Contratos</a>.</body>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return HttpResponse('ok')
        else:
            return HttpResponseForbidden()
