"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.db.models import Q
from django.shortcuts import redirect
from .models import Contacts,Address,Phone,Date
from .forms import ContactForm,AddressForm,PhoneForm,DateForm
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    All = Contacts.objects.all()
    q=request.GET.get("q")
    if q:
        All=All.filter(
            Q(addresses__Address__icontains=q)|
            Q(addresses__City__icontains=q)|
            Q(addresses__State__icontains=q)|
            Q(addresses__Zip__icontains=q)|
            Q(phones__Area_code__icontains=q)|
            Q(phones__Number__icontains=q)|
            Q(dates__Date__icontains=q)|    
            Q(Fname__icontains=q)|
            Q(Mname__icontains=q)|
            Q(Lname__icontains=q)      
            ).distinct()
    return render(
        request,
        'MainModule/index.html',
        {
            'Contacts':All,
        }
    )

def  ViewFullContact(request,pk):
    Contact=Contacts.objects.get(id=pk)
    AllAddress=Address.objects.filter(Contact_id=pk)
    AllPhones=Phone.objects.filter(Contact_id=pk)
    AllDates=Date.objects.filter(Contact_id=pk)

    form=ContactForm(request.POST or None ,instance=Contact)
    if form.is_valid():
        form.save()

    return render(request ,'MainModule/ViewFullContact.html', {'form' : form ,'Contact':Contact,'AllAddress' : AllAddress ,'AllPhones':AllPhones,'AllDates':AllDates })

def CreateContact(request):

    form=ContactForm(request.POST or None )
    if form.is_valid():
        form.save()
    return render(request ,'MainModule/ViewFullContact.html', {'form' : form} )

def UpdateContact(request,pk):
    Contact=Contacts.objects.get(id=pk)
    AllAddress=Address.objects.filter(Contact_id=pk)
    AllPhones=Phone.objects.filter(Contact_id=pk)
    AllDates=Date.objects.filter(Contact_id=pk)

    form=ContactForm(request.POST or None ,instance=Contact)
    if form.is_valid():
        form.save()
    return render(request ,'MainModule/ViewFullContact.html', {'form' : form ,'Contact':Contact,'AllAddress' : AllAddress ,'AllPhones':AllPhones,'AllDates':AllDates })

def DeleteContact(request,pk):
    Contact=Contacts.objects.get(id=pk)
    Contact.delete()
    return redirect('home')




def NewAddress(request):
    form=AddressForm(request.POST or None )
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request ,'MainModule/ViewFullContact.html', {'form' : form })

def NewPhone(request):
    form=PhoneForm(request.POST or None )
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request ,'MainModule/ViewFullContact.html', {'form' : form })

def NewDate(request):
    form=DateForm(request.POST or None )
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request ,'MainModule/ViewFullContact.html', {'form' : form })


def UpdateAddress(request,pk):
    Add=Address.objects.get(id=pk)
    form=AddressForm(request.POST or None ,instance=Add)
    if form.is_valid():
        form.save()
    return render(request ,'MainModule/AddOrUpdateAddress.html', {'form' : form ,'Address':Add})

def UpdatePhone(request,pk):   
    Ph=Phone.objects.get(id=pk)
    form=PhoneForm(request.POST or None ,instance=Ph)
    if form.is_valid():
        form.save()
    return render(request ,'MainModule/AddOrUpdateAddress.html', {'form' : form ,'Address':Ph})
def UpdateDate(request,pk):
    
    Dt=Date.objects.get(id=pk)
    form=PhoneForm(request.POST or None ,instance=Dt)
    if form.is_valid():
        form.save()
    return render(request ,'MainModule/AddOrUpdateAddress.html', {'form' : form ,'Address':Dt})

def DeleteAddress(request,pk=None,ContactId=None):
    Add=Address.objects.get(id=pk)
    Add.delete()
    Contact=Contacts.objects.get(id=ContactId)
    form=ContactForm(request.POST or None ,instance=Contact)
    AllAddress=Address.objects.filter(Contact_id=ContactId)
    AllPhones=Phone.objects.filter(Contact_id=ContactId)
    AllDates=Date.objects.filter(Contact_id=ContactId)
    return render(request ,'MainModule/ContactEdit.html', {'form' : form ,'Contact':Contact,'AllAddress' : AllAddress ,'AllPhones':AllPhones,'AllDates':AllDates })


def DeletePhone(request,pk=None,ContactId=None):
    Ph=Phone.objects.get(id=pk)
    Ph.delete()
    Contact=Contacts.objects.get(id=ContactId)
    form=ContactForm(request.POST or None ,instance=Contact)
    AllAddress=Address.objects.filter(Contact_id=ContactId)
    AllPhones=Phone.objects.filter(Contact_id=ContactId)
    AllDates=Date.objects.filter(Contact_id=ContactId)
    return render(request ,'MainModule/ContactEdit.html', {'form' : form ,'Contact':Contact,'AllAddress' : AllAddress ,'AllPhones':AllPhones,'AllDates':AllDates })

def DeleteDate(request,pk=None,ContactId=None):
    Dt=Date.objects.get(id=pk)
    Dt.delete()
    Contact=Contacts.objects.get(id=ContactId)
    form=ContactForm(request.POST or None ,instance=Contact)
    AllAddress=Address.objects.filter(Contact_id=ContactId)
    AllPhones=Phone.objects.filter(Contact_id=ContactId)
    AllDates=Date.objects.filter(Contact_id=ContactId)
    return render(request ,'MainModule/ContactEdit.html', {'form' : form ,'Contact':Contact,'AllAddress' : AllAddress,'AllPhones':AllPhones,'AllDates':AllDates  })



def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'MainModule/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'MainModule/about.html',
        {
            'title':'About',
            'message':'Your MainModulelication description page.',
            'year':datetime.now().year,
        }
    )
