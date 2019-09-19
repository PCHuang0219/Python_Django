from django.shortcuts import render
import pygame, time
import cv2
#from VideoCapture import Device
from pygame.locals import *


# Create your views here.
# Current working html
def index(request):
    return render(request, "opencv/webcam01.html")


#Create your views here.
#initial verstion, sample working view
#def index(request):
#    return render(request, "opencv/opencv.html")



def ShowWebCam():
    pygame.init()
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=550)
    cam = Device()
    screen = pygame.display.set_mode((200, 200))
    pygame.display.set_caption('Casting...')
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
        try:
            time.sleep(4)
            cam.saveSnapshot('image.jpg')
        except:
            pass

