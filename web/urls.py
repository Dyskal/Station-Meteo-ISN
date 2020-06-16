from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', main),
    path('home/', home),
    path('daily/', daily),
    path('about/', about),
    path('graph.png', graph),
] + static(settings.STATIC_URL)
