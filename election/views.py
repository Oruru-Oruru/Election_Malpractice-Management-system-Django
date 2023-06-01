
from django.shortcuts import  render,redirect, HttpResponse
from django.urls import reverse
from . forms import NewUserForm, LocationForm,EvidenceForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate 
#from .pdf import html2pdf
from django.template import context
from .models import *

from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = context_dict
    html  = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % html)



def evidence(request):
	if request.method == 'POST':
		form = EvidenceForm(request.POST,request.FILES)
		if form.is_valid():
			model_instance = form.save()
			model_instance.save()
		else:
			return render(request,'evidence.html', {'form':form})
		return redirect('thanks')
	else:
		form = EvidenceForm()
		return render(request,'evidence.html', {'form':form})



def location(request):
	if request.method == 'POST':
		form= LocationForm(request.POST)
		if form.is_valid():
			model_instance=form.save()
			model_instance.save()
			
		return redirect('evidence')
	else:
		form = LocationForm()
		return render(request, 'location.html', {'form':form})
def index(request):
	# return redirect(reverse('category'))
    return render(request, 'home.html')


def thank(request):
	return render(request, 'thanks.html')

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			print('it was a valid submission')
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('category')
		else:
			print('invalid submission, aborting')
			return render(request=request, template_name="login.html", context={"login_form":form})

		
			
		messages.error(request,"Invalid username or password.")
	
		messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def register_request(request):
	if request.method == "POST":
		
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			print(f'the user {user} saved successfully')
			messages.success(request, "Thanks for registering. Pleaselogin to continue." )
		else:
			return render (request=request, template_name="register.html", context={"register_form":form})

		return redirect('login')
	messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})




def category_detail(request, slug):
	category = Category.objects.get(id=slug)
	return render(request,'category_detail.html',{'category':category})

def category(request):
	categorie = Category.objects.all()
	
	return render(request,'category.html',{'categorie':categorie})


def logout_user(request):
    logout(request)
    messages.success(request, "Thanks You for Reporting!", extra_tags='alert alert-warning alert-dismissible fade show')

    return redirect('/')


def pdf(request):
    #Retrieve data or whatever you need
	results = []

	for x in Evidence.objects.all():
		data = {

		}
		print(x.evidence)
		data['name'] = x.reporter.username
		data['evidence'] = x.evidence
		data['location'] = x.location.County_name
		data['category'] = x.category.category_name
		results.append(data)

	
	return render_to_pdf(
	'pdf.html',
	{
	'pagesize':'A4',
	'data': results,
	}
	)

# def pdf(request):
# 	global pdf
# 	pdf=html2pdf('pdf.html')
# 	return HttpResponse(pdf, content_type="application/pdf ")




