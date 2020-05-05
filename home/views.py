from django.shortcuts import render

def home_page(request):
	return render(request, 'home.html')

def add(request):
	val1 = int(request.GET['salary'])
	pension = val1*0.1
	tax = (val1-(val1*0.1)-42500)*0.1
	sum1 = val1-(val1*0.1)-tax
	return render(request, "result.html", {'result': pension, 'result2': tax, 'result3': sum1,})