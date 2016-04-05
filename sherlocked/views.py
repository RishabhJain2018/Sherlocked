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
import datetime
def home(request):

	"""this view is for the home page display"""

	if request.user.is_authenticated():
		return render_to_response("description.html",{"user":request.user},context_instance=RequestContext(request))
	else:
		return render_to_response("index.html",{"user":0},context_instance=RequestContext(request))


def signup(request):

	"""signup for the user """

	if not request.user.is_active:
		if request.POST:
			print "entered the if section"
			username = request.POST['username']
			email = request.POST['email']
			password = request.POST['password']
			name = request.POST['firstname']
			college = request.POST['college']
			phno = request.POST['phno']
			try:
				user = User.objects.create_user(username=username,email=email,password=password,first_name=name,last_name='')
				user.save()
				UserDetail.objects.create(Zealid = username,college = college,phno = phno,LastSolvedAt = str(datetime.datetime.now())).save()
				return HttpResponseRedirect("/login")
			except:
				return render_to_response("register.html",{"error":1},context_instance = RequestContext(request))
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
				return HttpResponseRedirect("/description")
			else:
				# Show an error page
				return render_to_response("login.html",{"error":1},context_instance = RequestContext(request))
		return render_to_response('login.html',context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/mystery")

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

def description(request):
	""" profile editing view. User can update their profile using this view. """
	if request.user.is_authenticated():
		return render_to_response("description.html")
	else:
		return HttpResponseRedirect("/")

def mystery(request):
	if request.user.is_authenticated():
		user = UserDetail.objects.get(Zealid = request.user.username)
		if user.CurrentQuestionNo != 0:
			print "the username of user is ", request.user.username
			print "HE IS A PREVIOUS USER"
			print user.CurrentQuestionNo
			print "CURRENTLY THE USER IS AT ",user.CurrentQuestionNo
			if user.CurrentQuestionNo==17:
				return HttpResponseRedirect("/winner")
			question = Question.objects.get(pk = user.CurrentQuestionNo)
			print "user last solved at ", user.LastSolvedAt
			LastSolved = datetime.datetime.strptime(str(user.LastSolvedAt).split(".")[0], '%Y-%m-%d %H:%M:%S')
			wait = (datetime.datetime.now()-LastSolved).total_seconds() < float(question.WaitTime)*60*60 
			if wait:
				wt = abs((datetime.datetime.now()-LastSolved).total_seconds() - float(question.WaitTime)*60*60)
				print "THE WAIT TIME FOR USER IS ", wt 
				return render_to_response("question.html",{'wt':int(wt),'waitmsg':question.WaitMessage},context_instance = RequestContext(request))
			# waitTime = int((datetime.datetime.now() - user.LastSolvedAt[:-6]).total_seconds())
			# if waitime>=question.:
				# return render_to_response("question.html",{"wait":waititme},context_instance = RequestContext(request))
			# else:
			return render_to_response("question.html",{"q": question },context_instance = RequestContext(request))
		else:
			print "HE IS A NEW USER"
			UserDetail.objects.filter(Zealid = request.user.username).update(CurrentQuestionNo = 1,LastSolvedAt = str(datetime.datetime.now()))
			question = Question.objects.get(pk= 1)
			return render_to_response("question.html",{"q": question},context_instance =RequestContext(request))
		# waitTime = datetime.now() - user.LastSolvedAt
		return render_to_response('question.html')
	else:
		return HttpResponseRedirect('/')


def submit(request):
	if request.POST:
		print "entered into submit url"
		answer = request.POST['answer']
		user = UserDetail.objects.get(Zealid = request.user.username)
		question = Question.objects.get(pk = user.CurrentQuestionNo)
		if answer.lower() == question.Answer.lower():
			UserDetail.objects.filter(Zealid = request.user.username).update(CurrentQuestionNo = (user.CurrentQuestionNo)+1,LastSolvedAt = str(datetime.datetime.now()))
			print "The answer is correct and query executed "
		else:
			print "the answer is not correct."
	return HttpResponseRedirect("/mystery")

def leaderboard(request):
	users = UserDetail.objects.order_by('-CurrentQuestionNo')[:7:1]
	# if user.count()>10:
		# user = user[]
	# for i in users:
		# print i.Zealid
	return render_to_response("leaderboard.html",{'users':users},context_instance = RequestContext(request))

def winner(request):
	if user.is_authenticated():
		return render_to_response("winner.html")
	else:
		return HttpResponseRedirect("/")

def rules(request):
	return render(request, 'rules.html')