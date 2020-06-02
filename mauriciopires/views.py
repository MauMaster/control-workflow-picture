from django.shortcuts import render, redirect, HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.db import transaction
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models import Avg
from django.db.models import Count
from django.db.models import F
from django.db.models import CharField
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse
from datetime import datetime

from .filters import ImagesFilter, PaymentFilter


from .models import (
    Photographers,
    Images,
    Payment
)

from .forms import (
    PhotographersForm,
    ImagesForm,
    PaymentForm
)


def index(request):
    usuario = Photographers.objects.all()
    form = Photographers()
    data = {'usuario': usuario, 'form': form}
    return render(request, 'index.html', data)


@login_required
def paneladmin(request):
    images = Images.objects.all()
    data = { 'images': images}
    
    return render(
        request, 'paneladmin/index.html', data)

@login_required
def alluser(request):
    allusers = Photographers.objects.all()
    data = { 'allusers': allusers}
    return render(
        request, 'paneladmin/alluser.html', data)
   


def register(request):
    usuario = Photographers.objects.all()
    form = PhotographersForm()
    data = {'usuario': usuario, 'form': form}
    return render(request, 'paneladmin/register.html', data)

@transaction.atomic
def new_register(request):
    if request.method == 'POST':
        form = PhotographersForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.is_staff = True
            user = form.save()
            user.refresh_from_db()  
            user.photographers.name = form.cleaned_data.get('name')
            user.photographers.lastname = form.cleaned_data.get('lastname')
            user.photographers.email = form.cleaned_data.get('email')
            user.photographers.picture = form.cleaned_data.get('picture')
            user.photographers.phone = form.cleaned_data.get('phone')
            user.photographers.cpf = form.cleaned_data.get('cpf')
            user.photographers.cnpj = form.cleaned_data.get('cnpj')
            user.photographers.birthday = form.cleaned_data.get('birthday')
            user.photographers.picture = form.cleaned_data.get('picture')
            user.photographers.address = form.cleaned_data.get('address')
            user.photographers.number = form.cleaned_data.get('number')
            user.photographers.district = form.cleaned_data.get('district')
            user.photographers.zip_code = form.cleaned_data.get('zip_code')
            user.photographers.city = form.cleaned_data.get('city')
            user.photographers.state = form.cleaned_data.get('state')
            user.photographers.password1 = form.cleaned_data.get('password1')
            user.photographers.type_user = form.cleaned_data.get('type_user')
            username = form.cleaned_data.get('username')
            user.save()
            current_site = get_current_site(request)
            subject = 'Cadastro Mauricio Pires Edições de Imagens'
            message = render_to_string('paneladmin/html_email.html', {
                'user': user,
                'domain': current_site.domain,
                
            })
            user.email_user(subject, message)
            
            return redirect('paneladmin_index')
    else:
        form = PhotographersForm()
    return render(request, 'paneladmin/register.html', {'form': form})

def account_activation_sent(request):
    return render(request, 'paneladmin/account_activation_sent.html')

def images(request):
    images = Images.objects.all()
    form = ImagesForm()
    data = {'images': images, 'form': form}
    return render(request, 'paneladmin/images.html', data)


def register_images(request):
    
    if request.method == 'POST':
        form = ImagesForm(request.POST)
        if form.is_valid():
                   
            form.save()
            return redirect('paneladmin_index')
    else:
        form = ImagesForm()
    return render(request, 'paneladmin/images.html', {'form': form})



    


def payment(request):
    payment = Payment.objects.all()
    form = PaymentForm()
    data = {'payment': payment, 'form': form}
    return render(request, 'paneladmin/payment.html', data)

def register_payment(request):
    
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
                   
            form.save()
            return redirect('paneladmin_index')
    else:
        form = PaymentForm()
    return render(request, 'paneladmin/payment.html', {'form': form})

    
def search(request):
    sales_list = Images.objects.all() 
    sales_filter = ImagesFilter(request.GET, queryset=sales_list)
    # na pesquisa abaixo para dar a soma, precisei passar como parametro o sales_filter.qs, assim elle vai da a soma apenas referente a pesquisa gerada no filtro e não em todo o BD
    # e passei a condição F que permite que eu trabalhe com dois campos distintos matematicos, no caso abaixo peguei o numero de fotos e multipliquei pelo preço que pode variar
    places_count = sales_filter.qs.aggregate(total_amount=Sum(F('pictures') * F ('price'),output_field=CharField()))
    places_pictures = sales_filter.qs.aggregate(total_amount_pictures=Sum('pictures'))
    return render(request, 'paneladmin/sales_list.html', {'filter': sales_filter, 'places_count': places_count, 'places_pictures': places_pictures})

def search2(request):
    payment_list = Payment.objects.all() 
    payment_filter = PaymentFilter(request.GET, queryset=payment_list)
    places_count = payment_filter.qs.aggregate(total_amount=Sum(F('value'),output_field=CharField()))
        

    sales_list = Images.objects.all() 
    sales_filter = ImagesFilter(request.GET, queryset=sales_list)
    places_count2 = sales_filter.qs.aggregate(total_amount_sale=Sum(F('pictures') * F ('price'),output_field=CharField()))
    places_pictures = sales_filter.qs.aggregate(total_amount_sale=Sum('pictures'))
        
   
    return render(request, 'paneladmin/payments_list.html', {'filter': payment_filter,  'places_count': places_count, 'places_count2': places_count2, 'places_pictures':places_pictures})

def ImagesUpdate(request,  id):
    

    comentario_delete = Images.objects.get(pk=id)
    return render(request, 'paneladmin/images_update.html')
        
       
       

   


  