from django.shortcuts import render, redirect
from subprocess import PIPE, Popen, STDOUT
from sys import executable
from os.path import dirname


def main(request):
    out = Popen([executable, dirname(dirname(__file__)) + "/gui/getdata.py"], shell=False, stdout=PIPE, stderr=STDOUT,
                universal_newlines=True).communicate()[0].strip()
    result = out.split("\n", 3)
    return render(request, "homepage.html",
                  {'time': result[0], 'temp': result[1], 'pressure': result[2], 'humidity': result[3]})


def home(request):
    return redirect('/')


def daily(request):
    return render(request, "daily.html")


def about(request):
    return render(request, "about.html")
