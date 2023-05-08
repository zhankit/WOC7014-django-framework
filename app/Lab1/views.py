import random
from django.shortcuts import render
# import numpy as np

# Create your views here.

def question1(request):
    
	food = ["fat", "protein", "vitamin", "noodles", "rice"]
	index = random.randint(0, len(food) - 1)
	context = {
		"food": food[index],
	}

	return render(request, "question1.html", context)


def question2(request):
	pattern = ""
	for x in range (1, 8):
		for y in range (1, x):
			pattern += "#" 
		pattern +=  "\n"

	for x in range (1, 3):
			for y in range (1, 3):
				pattern += "#" 
			pattern +=  "\n"

	context = {
		"pattern": pattern,
	}
	return render(request, "question2.html", context)


def question3(request):

	TOTAL_COURSE = 6

	subject = []
	credits_hours = []
	total_hours = 0
	result = 0
	
	for x in range (0 , TOTAL_COURSE):
		temp_subj = random.randint(0, 100)
		temp_credit = random.randint(20, 40)

		subject.append(temp_subj)
		credits_hours.append(temp_credit)

		result += temp_subj * temp_credit
		total_hours += temp_credit

	result = round(result / total_hours,2)

	cgp = ""
	if (result < 35): cgp = 0.0
	# elif (result < 35): cgp = 1.0
	elif (result < 40): cgp = 1.0
	elif (result < 45): cgp = 1.5
	elif (result < 55): cgp = 1.7
	elif (result < 60): cgp = 2.0
	elif (result < 65): cgp = 2.3
	elif (result < 70): cgp = 2.7
	elif (result < 75): cgp = 3.0
	elif (result < 80): cgp = 3.3
	elif (result < 90): cgp = 3.7
	elif (result <= 100): cgp = 4.0
	# else: cgp = 4.0

	context = {
		"subject": subject,
		"credits_hours": credits_hours,
		"result": result,
		"cgp": cgp
	}

	return render(request, "question3.html", context)
