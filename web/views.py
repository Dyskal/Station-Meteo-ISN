from django.shortcuts import render, redirect, HttpResponse
from subprocess import PIPE, Popen, STDOUT
from sys import executable
from os.path import dirname
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np


def main(request):
    out = Popen([executable, dirname(dirname(__file__)) + "/gui/data.py"], shell=False, stdout=PIPE, stderr=STDOUT,
                universal_newlines=True).communicate()[0].strip()
    result = out.split("\n", 3)
    return render(request, "homepage.html",
                  {'time': result[0], 'temp': result[1], 'pressure': result[2], 'humidity': result[3]})


def home(request):
    return redirect("/")


def daily(request):
    return render(request, "daily.html")


def graph(request):
    plt.style.use('bmh')
    fig = plt.figure(figsize=(16, 9))
    ax = plt.axes()
    plt.title("Humidité (dernières 24h)", color="white", size="30")

    x = np.linspace(0, 10, 1000)
    ax.plot(x, np.sin(x))

    plt.grid(color='white')
    ax.tick_params(colors='white')
    for tick in ax.get_xticklabels():
        tick.set_color('white')
    for tick in ax.get_yticklabels():
        tick.set_color('white')

    buf = BytesIO()
    plt.savefig(buf, transparent=True, bbox_inches='tight', format='png')
    plt.close(fig)
    return HttpResponse(buf.getvalue(), content_type='image/png')


def about(request):
    return render(request, "about.html")
