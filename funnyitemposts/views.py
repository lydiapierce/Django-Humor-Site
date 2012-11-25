# Create your views here.
from django.shortcuts import render_to_response
from django.http import Http404
from funnyitemposts.models import Funnyitempost
 
def home(request):
	return render_to_response("home.html",{
		"funnyitemposts" : Funnyitempost.objects.all().order_by('displayedat')
	})
 
def funnyitempost_specific(request, funnyitempost_id):
	try:
		p = Funnyitempost.objects.get(pk=funnyitempost_id)
	except:
		raise Http404
 
	return render_to_response("funnyitempost_specific.html",{
		"funnyitempost" : p
	})