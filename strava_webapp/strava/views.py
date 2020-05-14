from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from stravaio import strava_oauth2
from stravaio import StravaIO

MY_STRAVA_CLIENT_ID = '44247'
MY_STRAVA_CLIENT_SECRET = '7224bbf5323a86ee18e2fafb5fe084d52991474c'

# Create your views here.
def home(request):
	return render(request, 'strava/home.html')

def stravaAuthentication(request):
	print('check')
	auth_res = strava_oauth2(client_id=MY_STRAVA_CLIENT_ID, client_secret=MY_STRAVA_CLIENT_SECRET)
	client = StravaIO(access_token=auth_res['access_token'])
	athlete = client.get_logged_in_athlete()
	athlete = athlete.to_dict()
	print(athlete)
	return HttpResponse("Athlete Authenticated: " + athlete['firstname'])

def sampleData(request):
	return HttpResponse("In sample data ")