import random
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def helloworld_view(request):
    return HttpResponse("Hello 'Django' World!")


def logicaldecision_view(request):
	weather = ["rainy", "sunny"]
	randomforecast = random.randint(0, 1)
	umbrella_result = ''
        
	if weather [randomforecast] == "rainy":
		umbrella_result = 'will'
	else:
		umbrella_result = 'will not'
	
	context = {
		"weather_result": str(weather[randomforecast]),
		"umbrella_result": umbrella_result,
	}

	return render(request, "weatherForecast.html", context)


def loop_view(request):
	i = 1
	result = " "
	while i <= 6: 
		result = result + "# "
		i += 1

	for_result = " "
	for x in range (2, 30, 4):
		for_result = for_result + str(x) + ""

	context = {
		"while_result": result,
		"for_result": for_result,
	}

	return render(request, "loop.html", context)
