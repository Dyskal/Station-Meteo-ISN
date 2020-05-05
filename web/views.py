from django.shortcuts import render
from subprocess import PIPE, Popen, STDOUT
from sys import executable
from os import getcwd


def main(request):
    out = Popen([executable, getcwd()+"/gui/getdata.py"], shell=False, stdout=PIPE, stderr=STDOUT,
                universal_newlines=True).communicate()[0].strip()
    result = out.split("\n", 3)
    return render(request, "main.html",
                  {'time': result[0], 'temp': result[1], 'pressure': result[2], 'humidity': result[3]})
