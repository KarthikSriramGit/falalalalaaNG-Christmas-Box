#~~~~~~~~~~~WELCOME to falalalalaNG.py~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~ECE-GY 6183 DSP LAB: Final Project~~~~~~~~~~~~~~~~oo
#~~~~~~~~Vanshika Sachdev & Karthik Sriram~~~~~~~~~~~~~~~~~
#~~~~~~~~~~falalalalaNG Christmas Box~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import cv2
import numpy as np
import math
import sys
import pygame
import time
    #~~~~~~~~~~~~~GUI~~~~~~~~~~~~~~~~
import tkinter
from tkinter import *
from tkinter import Tk, Frame, BOTH
from PIL import Image, ImageTk
root = Tk()
root.title('falalalalaaNG Christmas Box')
im = Image.open('falalalalaaNG.jpg')
tkimage = ImageTk.PhotoImage(im)
myvar = tkinter.Label(root, image=tkimage)
myvar.place(relx=0.5, rely=0.735, anchor=CENTER)
playing=True
def check():
    if playing:
        print("Enjoy Playing")
root.after(1000, check)
def NewYear():
    global playing
    root.destroy()
    sys.exit()
    playing=False
def Christmas():
    global playing
    #~~~~TEXT TO SPEECH CONVERTER~~~~~~
    import pyttsx3
    engine = pyttsx3.init()
    #~~~~~~AUDIO EMBEDDING OF BGM: CHRISTMAS POPS!~~~~~~~
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load('Christmas_Box_Pops.mp3')
    pygame.mixer.music.play()
    pygame.init()

    #-------------------------------------------------------
    #Input acquisition through the in-built Web-Camera
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    import time
    Bookface = cv2.CascadeClassifier('Game.xml') #Cascade Haar Classifier variable
    catchemall = cv2.VideoCapture(0)

    #~~~~~~Initialization~~~~~~
    #No of gifts
    gifts = 0
    # Level of the game you are at
    age = 1
    # Levels of victory:
    vk = 0
    #Locking parameter x
    thalax = 0
    #Locking parameters y
    pootuy = 0
    #Success/Advancement parameter
    jeeth = 0
    #Ending parameter
    khatam = 40
    #Starting parameters
    aaramb = 1
    intro = 0
    #Position check
    desi = 1
    #Failure/Loss Parameter which gives luck!
    luck = 0
    #Failure acknowledgement parameter
    har = 0
    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    #~~~~~~~Presentation the frame of the game~~~~~~~~~~~~~~~~~~~~~~~~ 
    #~~~Margins/Boundaries~~~~~~
    TPCR = (500, 30) 
    C = (250, 250)#~~~~~Middle
    BLCT = (500, 60)
    #~~~~Font Parameters~~~~~~~~
    #Hershey Font
    Fonte = cv2.FONT_HERSHEY_SIMPLEX
    #Font colour
    Fonterang = (255, 255, 255)
    #Font dimensions
    Fontealavu = 1
    koducode = 2
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #~~~~~~~~Execution of the Game! Ready to Rumble?~~~~~~~~~~~~~~~~~~
    # 1F@T
    while True:
        #Reads the square frame dimensions
        ret, square = catchemall.read()
        #Provides the Christmas colours of green and red to the frame
        grey = cv2.cvtColor(square, cv2.COLOR_BGR2GRAY)
        #Detection of the fist/hand within the frame
        moonjis = Bookface.detectMultiScale(
            grey,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(70, 70),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
    #~~~~~~~~Find and catch the gift!~~~~~
        #Parameters of axis x and y, width w and height h
        for (x, y, w, h) in moonjis:
            #Most important function that forms the image detection-cv2.rectangle
            cv2.rectangle(square, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #Once frame is formed, the level parameter is increased!
            vk = vk + 1 
    #~~~~~~~~Begin here!~~~~~~~
            #The starting parameter is checked for printing
            if aaramb == 1:
                #Gives you a counter to start the game
                print('Are you ready?')
                #Check 1-Delay 1
                time.sleep(1);
                #Check 2-Delay 2
                print('Ready')
                #Check 3- Delay 3
                time.sleep(1);
                print('Steady')
                time.sleep(1);
                #Start!-Follow the instruction
                print('Make a fist!')
                #Starting parameter is modified
                aaramb = 2
    #~~~~~~~~~~~~~~~~~~~~~~~~~GIFTS MATCH AND COUNT~~~~~~~~~~~~~~~~~~~~~~~
            if vk % 20 == 0:
                thalax = x
                pootuy = y #Locking parameters latching onto the part of the body
                if desi == 1 and aaramb == 2:
                    cv2.rectangle(square, (400, 200), (640, 440), (0, 0, 255), 3)
                    #Positions of the red rectangle(x,y) and its w and h. 
                    #The values need to match with the green rectangle.
                    if x > 407 and y > 208 and y < 332 and w < 228:
                        desi = 2
                        har = 0
                        gifts = gifts + 100
                        print('Your help so far:', gifts)
                        engine.say(gifts)
                        engine.runAndWait()
                    if vk % khatam == 0:
                        har = har + 1
                    if har == 6:
                        desi = 10
                if desi == 2:
                    cv2.rectangle(square, (100,200), (340, 440), (0, 0, 255), 3)
                    if x > 95 and x < 225 and y > 208 and y < 342 and w < 210:
                        desi = 3
                        har = 0
                        gifts = gifts + 100
                        print('Your help so far:', gifts)
                        engine.say(gifts)
                        engine.runAndWait()
                    if vk % khatam == 0:
                        har = har + 1
                    if har == 6:
                        desi = 10
                if desi == 3:
                    cv2.rectangle(square, (400, 100), (640, 340), (0, 0, 255), 3)
                    if x > 400 and x < 515 and y > 105 and y < 230 and w < 228:
                        desi = 4
                        har = 0
                        gifts = gifts + 100
                        print('Your help so far:', gifts)
                        engine.say(gifts)
                        engine.runAndWait()
                    if vk % khatam == 0:
                        har = har + 1
                    if har == 6:
                        desi = 10
                if desi == 4:
                    cv2.rectangle(square, (100, 100), (340, 340), (0, 0, 255), 3)
                    if x > 100 and x < 227 and y > 108 and y < 198 and w < 228:
                        desi = 5
                        har = 0
                        gifts = gifts + 100
                        print('Your help so far:', gifts)
                        engine.say(gifts)
                        engine.runAndWait()
                    if vk % khatam == 0:
                        har = har + 1
                    if har == 6:
                        desi = 10
                if desi == 5:
                    cv2.rectangle(square, (200, 200), (440, 440), (0, 0, 255), 3)
                    if x > 195 and x < 325 and y > 208 and y < 342 and w < 210:
                        desi = 6
                        har = 0
                        gifts = gifts + 100
                        print('Your help so far:',gifts)
                        engine.say(gifts)
                        engine.runAndWait()
                    if vk % khatam == 0:
                        har = har + 1
                    if har == 6:
                        desi = 10
                if desi == 6:
                    cv2.rectangle(square, (400, 100), (640, 340), (0, 0, 255), 3)
                    if x > 400 and x < 515 and y > 105 and y < 230 and w < 228:
                        desi = 7
                        har = 0
                        gifts = gifts + 100
                        print('Your help so far:', gifts)
                        engine.say(gifts)
                        engine.runAndWait()
                    if vk % khatam == 0:
                        har = har + 1
                    if har == 6:
                        desi = 10
                if desi == 7:
                    cv2.rectangle(square, (100, 100), (340, 340), (0, 0, 255), 3)
                    if x > 100 and x < 227 and y > 108 and y < 198 and w < 228:
                        desi = 8
                        har = 0
                        gifts = gifts + 100
                        print('Your help so far:', gifts)
                        engine.say(gifts)
                        engine.runAndWait()
                    if vk % khatam == 0:
                        har = har + 1
                    if har == 6:
                        desi = 10
                if desi == 8:
                    cv2.rectangle(square, (400, 200), (640, 440), (0, 0, 255), 3)
                    if x > 407 and y > 208 and y < 332 and w < 228:
                        desi = 9
                        har = 0
                        gifts = gifts + 100
                        print('Your help so far:', gifts)
                        engine.say(gifts)
                        engine.runAndWait()
                    if vk % khatam == 0:
                        har = har + 1
                    if har == 6:
                        desi = 10
                if desi == 9:
                    print('Congratulations! You WON!!')
                    print('All of the number', age, 'stage is done')
                    khatam = khatam - 10
                    age = age + 1
                    if age == 2:
                        print('Meh. You are getting there.')
                    if age == 3:
                        print('You are on fire!')
                    if age < 4:
                        print('Next Ride');
                        time.sleep(1);
                        print('Merry')
                        time.sleep(1);
                        print('Merry')
                        time.sleep(1);
                        print('Christmas')
                        desi = 2
                    if age == 4:
                        jeeth = 1; #YOU WON! GAME OVER.
                        break
                if desi == 10:
                    #MUMUMUAHMUAHMOOOOOH 
                    print('Better luck next time!');
                    #Give 'em the luck
                    luck = 1;            
        square = cv2.flip(square, 1)
        cv2.putText(square, str(gifts), BLCT, Fonte, Fontealavu, Fonterang, koducode)
        cv2.putText(square, 'Gifts!:',TPCR, Fonte, Fontealavu, Fonterang, koducode)
        cv2.imshow('Video', square)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            pygame.mixer.music.stop()
            break
        if jeeth == 1:
            pygame.mixer.music.stop()
            break
        if luck == 1:
            pygame.mixer.music.stop()
            break
        if playing == False:
            pygame.mixer.music.stop()
            break
        
    catchemall.release()
    cv2.destroyAllWindows()
#~~~~~~~~~~~~~~~~~~~SURPRISE!~~~~~~~~~~~~~~~~~~~~~~~~~
#Intended just to present a surprise Christmas gift to the DSP Lab team.
def surprise():
    import pyglet
    ag_file = "ChristmasSurprise.gif"
    animation = pyglet.resource.animation(ag_file)
    sprite = pyglet.sprite.Sprite(animation)
    win = pyglet.window.Window(width=sprite.width, height=sprite.height)
    green = 0, 1, 0, 1
    pyglet.gl.glClearColor(*green)
    @win.event
    def on_draw():
        win.clear()
        sprite.draw()
    pyglet.app.run()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~FINAL GUI FORMATTING~~~~~~~~~~~~~~~~
#Main head
t = Label(root, text='ECE-GY 6183 DSP Final Project')
t.config(width=75)
t.config(font=('Helvetica', 30))
t.pack()
#Main title for button1
x1 = Label(root, text='Christmas Box: Help Santa fill his sleigh!Click Play to catch gifts!')
x1.config(width=75)
x1.config(font=('Helvetica', 30))
x1.pack()
#Play:Merry Christmas button1
bu1 = Button(root, text='Play: Merry Christmas!', command=Christmas, bg='green')
bu1.config(font=('Times New Roman', 35, 'bold'))
bu1.pack()
#Main title for button2
x2 = Label(root, text='Click to end the fun and proceed to New Year!')
x2.config(width=75)
x2.config(font=('Helvetica', 30))
x2.pack()
#End: Next stop:Happy New Year button2
bu2 = Button(root, text='End: Next stop:Happy New Year!', command=NewYear, bg='red')
bu2.config(font=('Raavi', 35, 'bold'))
bu2.pack()
#Main title for button3
x3 = Label(root, text='Ready to be surprised? Click below!')
x3.config(width=75)
x3.config(font=('Helvetica', 30))
x3.pack()
#Surprise!Happy Holidays! button3
bu3 = Button(root, text='Surprise!Happy Holidays!', command=surprise, bg='purple')
bu3.config(font=('Times New Roman', 35, 'bold'))
bu3.pack()
#Function calls checker
root.after(1000, check)
root.mainloop()
#~~~~~~~~~~~~~~~~~~~~~~~~~BIBLIOGRAPHY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GIF Function: https://www.daniweb.com/programming/software-development/code/217060/show-animated-gif-files-python
#~~~~~~~~~~~~~~~~~MERRY CHRISTMAS AND HAPPY NEW YEAR!~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~THANK YOU~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~THE END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
