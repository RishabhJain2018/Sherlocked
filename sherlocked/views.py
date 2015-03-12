from django.shortcuts import render
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import *
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from sherlocked.models import * 
from datetime import datetime,timedelta
import random,string,ast
def home(request):
	"""this view is for the home page display"""
	return render_to_response("index.html",context_instance=RequestContext(request))

def signup(request):
	"""signup for the user """
	if not request.user.is_active:
		if request.POST:
			print "entered the if sectison"
			username = request.POST['username']
			email = request.POST['email']
			password = request.POST['password']
			name = request.POST['firstname']
			try:
				user = User.objects.create_user(username=username,email=email,password=password,first_name=name,last_name='')
				user.save()
				return HttpResponseRedirect("/login")
			except:
				return HttpResponse("<h2>Error: This Id already exists</h2>")
		else:
			print "entered the else section"
			return render_to_response("register.html",context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/")	

def login(request):
	""" Login view """
	if not request.user.is_authenticated():
		if request.POST:
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=username, password=password)
			if user is not None and user.is_active:
				# Correct password, and the user is marked "active"
				auth.login(request,user)
				# Redirect to a success page.
				return HttpResponseRedirect("/profile")
			else:
				# Show an error page
				return HttpResponse("<h3>Incorrect password</h3>")
		return render_to_response('login.html',context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/profile")

# def changepassword(request):
# 	""" user password change view """
# 	if user.is_authenticated:
# 		if request.POST:
# 			username = user.username
# 			# email = request.POST['email']
# 			password = request.POST['password']
# 			user = User.objects.get(username=username)
# 			user.set_password(password)
# 			user.save()
# 	return HttpResponseRedirect("/passwordrofile")

# donot delete this function as it may be used in future for the purpose of logout to a specific page
# def logout_view(request):
	# """logout view """
# 	logout(request)
# 	# return HttpResponseRedirect("/")
# 	return render_to_response("index.html",{'logout':1},context_instance=RequestContext(request))

def profile(request):
	""" profile editing view. User can update their profile using this view. """
	return HttpResponse("THIS IS PROFILE PAGE")

def mystery(request):
	if request.user.is_authenticated():
		try:
			user = UserDetail.objects.get(Zealid = request.user.username)
			question = Question.objects.get(pk = user.CurrentQuestionNo)
			return render_to_response("question.html",{"q":question},context_instance = RequestContext(request))
		except:
			UserDetail.objects.create(Zealid = request.user.username, CurrentQuestionNo = 1).save()
			question = Question.objects.get(pk= 1)
			return render_to_response("question.html",{"q":question},context_instance =RequestContext(request))
		# waitTime = datetime.now() - user.LastSolvedAt
		return render_to_response('question.html')
	else:
		return HttpResponseRedirect('/login')

def submit(request):
	if request.POST:
		answer = request.POST['answer']
		user = UserDetail.objects.get(Zealid = request.user.username)
		question = Question.objects.get(pk = user.CurrentQuestionNo)
		if answer.lower() == question.Answer.lower():
			UserDetail.objects.filter(Zealid = request.user.username).update(CurrentQuestionNo = user.CurrentQuestionNo+1)
			return HttpResponseRedirect("/mystery")


