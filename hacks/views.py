from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import generic
from django.views.generic.edit import FormView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail

from hacks.models import Hackathon, CodeMania
from hacks.forms import HackathonForm
from .forms import HackathonForm, CodeManiaForm

import json

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


# Create your views here.

class HackathonView(generic.View):
	def get(self, request):
		form = HackathonForm
		template_name = 'index.html'
		return render(request, template_name)

	def post(self, request):
		try:
			# f = HackathonForm(request.POST)
			# f.save()
			name = request.POST.get('name', None)
			email = request.POST.get('email',None )
			phone_number = request.POST.get('phone_number', None)
			github = request.POST.get('github', None)
			linkedin = request.POST.get('linkedin', None)
			hardware_required= request.POST.get('hardware_required', None)
			mac_address= request.POST.get('mac_address', None)
			size = request.POST.get('size', None)
			Hackathon.objects.create(name = name, email=email, phone_number=phone_number, github=github, linkedin=linkedin, hardware_required = hardware_required, mac_address=mac_address, size=size)
			plaintext = get_template('registration_email.txt')
			htmly     = get_template('registration_email.html')

			d = Context({ 'name': request.POST.get('name', None) })

			subject, from_email, to = 'Hackathon-2015', 'Microsoft Mobile Innovation Lab <mmil@jssaten.ac.in>', request.POST.get('email', )
			text_content = plaintext.render(d)
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			# send_mail('Hackathon-2015', 'Here is the message.', 'Microsoft Mobile Innovation Lab <mmil@jssaten.ac.in>', ['deshrajdry@gmail.com'], fail_silently=False)
			return HttpResponse(json.dumps({"event":1}), content_type="application/json")
		except Exception as e:
			return HttpResponse(json.dumps(e), content_type="application/json")

class CodeManiaView(generic.View):
	def get(self, request):
		form = CodeManiaForm
		template_name = 'codemania.html'
		return render(request, template_name, {'form':form})

	def post(self, request):
		try:
			f = CodeManiaForm(request.POST)
			f.save()
			# plaintext = get_template('registration_email.txt')
			# htmly     = get_template('registration_email.html')
			# d = Context({ 'name': request.POST.get('name', None) })

			# subject, from_email, to = 'CodeMania-2015', 'Microsoft Mobile Innovation Lab <mmil@jssaten.ac.in>', request.POST.get('email', )
			# text_content = plaintext.render(d)
			# html_content = htmly.render(d)
			# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
			# msg.attach_alternative(html_content, "text/html")
			# msg.send()
			# send_mail('Hackathon-2015', 'Here is the message.', 'Microsoft Mobile Innovation Lab <mmil@jssaten.ac.in>', ['deshrajdry@gmail.com'], fail_silently=False)
			return HttpResponse(json.dumps({"event":1}), content_type="application/json")
		except Exception as e:
			return HttpResponse(json.dumps(e), content_type="application/json")