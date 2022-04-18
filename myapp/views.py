from django.shortcuts import render
import random
import pyautogui
from django.conf import settings
from django.contrib import messages

def index(request):
    if request.method == "POST":
        ssvsvs = pyautogui.screenshot()
        imges = f'myimg{random.randint(1000,9999)}.png'
        ssvsvs.save(settings.MEDIA_ROOT/imges)
        messages.success(request,'screenshot has been taken')
        return render(request,'home.html',{'img':imges})
    return render(request,'home.html')
