from django.shortcuts import render
from django.http import HttpResponse
from . models import place
from . models import person


# Create your views here.
def home1(request):
    obj=place.objects.all()
    per=person.objects.all()
    return render(request, "index.html",{'result':obj,
                                         'persons':per})


# def calculate(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#
#     addition = x + y
#     subtraction = x - y
#     multiplication = x * y
#
#     if y != 0:
#         division = x / y
#     else:
#         division = "None"
#     return render(request, 'result.html',{'addition': addition,
#                                           'subtraction': subtraction,
#                                           'multiplication': multiplication,
#                                           'division': division})


