# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 17:44:11 2018

@author: austi
"""

import pygame
import pygame.midi
import sys
import time


BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
LIGHTRED = ( 255, 140, 140)
pygame.init()
pygame.midi.init()
#pygame.fastevent.init()
#event_get = pygame.fastevent.get
#event_post = pygame.fastevent.post

def print_device_info():
    for i in range( pygame.midi.get_count() ):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r

        in_out = ""
        if input:
            in_out = "(input)"


        return ("%2i: interface: %s, name: %s, opened: %s %s" %
               (i, interf, name, opened, in_out))


#|=========================
#|DrawPressedKey
#|=========================
#This function draws an outine over the key played on the kyeboard by the user 
#PARAMETERS:
# -bottomKey = The lowest key on the keyboard (in MIDI Notation) 
# -xStart = The leftmost point where the keyboard graphic starts
# -yPos   = The topmost point where the keyboard graphic starts
# -keyPlayed = the key played on the keyboard (in MIDI notation)
# -surface = The base surface to draw on
def DrawPressedKey(bottomKey, xStart, yPos, keyPlayed, surface):
    #xPos = xStart + 25*(keyPlayed - bottomKey)
    #Dynamically generate black keys
    xPos = xStart
    #RANDOM RECTANGLE:
    #pygame.draw.rect(surface,RED,pygame.Rect(xPos,yPos,25,155),1)
    
    #GetHighlightData will return updated xPos and yPos coordinates
    #It will also return which keyType to draw (4 different types)
    keyType = 0
    xPos, yPos, keyType = getHighlightData(keyPlayed, xPos, yPos)
    #print(keyType)
    if(keyType == 0): #Edge key
        pygame.draw.polygon(surface, LIGHTRED, ((xPos,yPos),(xPos,yPos+153),(xPos+24,yPos+153),(xPos+24,yPos+103),(xPos+14,yPos+103),(xPos+14,yPos)))
        pygame.draw.polygon(surface, RED, ((xPos,yPos),(xPos,yPos+153),(xPos+24,yPos+153),(xPos+24,yPos+103),(xPos+14,yPos+103),(xPos+14,yPos)), 2)
    if(keyType == 1):
        pygame.draw.polygon(surface, LIGHTRED, ((xPos,yPos),(xPos,yPos+99),(xPos+12,yPos+99),(xPos+12,yPos)))
        pygame.draw.polygon(surface, RED, ((xPos,yPos),(xPos,yPos+99),(xPos+12,yPos+99),(xPos+12,yPos)),2)
    if(keyType == 2):
        pygame.draw.polygon(surface, LIGHTRED, ((xPos,yPos),(xPos+12,yPos),(xPos+12,yPos+101),(xPos+17,yPos+101),(xPos+17,yPos+153),(xPos-5,yPos+153),(xPos-5,yPos+101),(xPos,yPos+101)))
        pygame.draw.polygon(surface, RED, ((xPos,yPos),(xPos+12,yPos),(xPos+12,yPos+101),(xPos+17,yPos+101),(xPos+17,yPos+153),(xPos-5,yPos+153),(xPos-5,yPos+101),(xPos,yPos+101)),2)        
    if(keyType == 3):
        pygame.draw.polygon(surface, LIGHTRED, ((xPos,yPos+102),(xPos+10,yPos+102),(xPos+10,yPos),(xPos+22, yPos),(xPos+22,yPos+153),(xPos,yPos+153)))
        pygame.draw.polygon(surface, RED, ((xPos,yPos+102),(xPos+10,yPos+102),(xPos+10,yPos),(xPos+22, yPos),(xPos+22,yPos+153),(xPos,yPos+153)),2)
    if(keyType == 4):
        pygame.draw.polygon(surface, LIGHTRED, ((xPos,yPos),(xPos,yPos+153),(xPos+24,yPos+153),(xPos+24,yPos+103),(xPos+11,yPos+103),(xPos+11,yPos)))
        pygame.draw.polygon(surface, RED, ((xPos,yPos),(xPos,yPos+153),(xPos+24,yPos+153),(xPos+24,yPos+103),(xPos+11,yPos+103),(xPos+11,yPos)), 2)
    if(keyType == 5):
        pygame.draw.polygon(surface, LIGHTRED, ((xPos,yPos),(xPos+11,yPos),(xPos+11,yPos+101),(xPos+19,yPos+101),(xPos+19,yPos+153),(xPos-5,yPos+153),(xPos-5,yPos+101),(xPos,yPos+101)))
        pygame.draw.polygon(surface, RED, ((xPos,yPos),(xPos+11,yPos),(xPos+11,yPos+101),(xPos+19,yPos+101),(xPos+19,yPos+153),(xPos-5,yPos+153),(xPos-5,yPos+101),(xPos,yPos+101)),2)
    #pygame.draw.rect(surface,RED,pygame.Rect((100,100), (130,170)))
    #MIDI on AlethaKeybaord goes from 36-96
    return True

def number_to_note(number):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    return notes[number%12]

def getHighlightData(keyPlayed, xPos, yPos):
    keyType = 0
    
    if(keyPlayed == 36):
        keyType = 0
    elif (keyPlayed == 37):
        keyType = 1
        xPos = xPos + 16
    elif (keyPlayed == 38):
        keyType = 2
        xPos = xPos + 31
    elif (keyPlayed == 39):
        keyType = 1
        xPos = xPos + 45
    elif (keyPlayed == 40):
        keyType = 3
        xPos = xPos + 51
    elif (keyPlayed == 41):
        keyType = 4
        xPos = xPos + 75
    elif (keyPlayed == 42):
        keyType = 1
        xPos = xPos + 89
    elif (keyPlayed == 43):
        keyType = 5
        xPos = xPos + 103
    elif (keyPlayed == 44):
        keyType = 1
        xPos = xPos + 118
    elif (keyPlayed == 45):
        keyType = 2
        xPos = xPos + 131
    elif (keyPlayed == 46):
        keyType = 1
        xPos = xPos + 146
    elif (keyPlayed == 47):
        keyType = 3
        xPos = xPos + 149
    elif (keyPlayed == 48):
        keyType = 4
        xPos = xPos + 174
        
    #Octave 2
        
    elif (keyPlayed == 49):
        keyType = 1
        xPos = xPos + 189
    elif (keyPlayed == 50):
        keyType = 2
        xPos = xPos + 204
    elif (keyPlayed == 51):
        keyType = 1
        xPos = xPos + 218
    elif (keyPlayed == 52):
        keyType = 3
        xPos = xPos + 224
    elif (keyPlayed == 53):
        keyType = 4
        xPos = xPos + 248
    elif (keyPlayed == 54):
        keyType = 1
        xPos = xPos + 262
    elif (keyPlayed == 55):
        keyType = 5
        xPos = xPos + 276
    elif (keyPlayed == 56):
        keyType = 1
        xPos = xPos + 291
    elif (keyPlayed == 57):
        keyType = 2
        xPos = xPos + 304
    elif (keyPlayed == 58):
        keyType = 1
        xPos = xPos + 319
    elif (keyPlayed == 59):
        keyType = 3
        xPos = xPos + 322
    elif (keyPlayed == 60):
        keyType = 4
        xPos = xPos + 347

    #Octave 3
        
    elif (keyPlayed == 61):
        keyType = 1
        xPos = xPos + 362
    elif (keyPlayed == 62):
        keyType = 2
        xPos = xPos + 377
    elif (keyPlayed == 63):
        keyType = 1
        xPos = xPos + 391
    elif (keyPlayed == 64):
        keyType = 3
        xPos = xPos + 397
    elif (keyPlayed == 65):
        keyType = 4
        xPos = xPos + 421
    elif (keyPlayed == 66):
        keyType = 1
        xPos = xPos + 435
    elif (keyPlayed == 67):
        keyType = 5
        xPos = xPos + 449
    elif (keyPlayed == 68):
        keyType = 1
        xPos = xPos + 464
    elif (keyPlayed == 69):
        keyType = 2
        xPos = xPos + 477
    elif (keyPlayed == 70):
        keyType = 1
        xPos = xPos + 492
    elif (keyPlayed == 71):
        keyType = 3
        xPos = xPos + 495
    elif (keyPlayed == 72):
        keyType = 4
        xPos = xPos + 520

#Octave 4
        
    elif (keyPlayed == 73):
        keyType = 1
        xPos = xPos + 534
    elif (keyPlayed == 74):
        keyType = 2
        xPos = xPos + 549
    elif (keyPlayed == 75):
        keyType = 1
        xPos = xPos + 563
    elif (keyPlayed == 76):
        keyType = 3
        xPos = xPos + 569
    elif (keyPlayed == 77):
        keyType = 4
        xPos = xPos + 593
    elif (keyPlayed == 78):
        keyType = 1
        xPos = xPos + 607
    elif (keyPlayed == 79):
        keyType = 5
        xPos = xPos + 620
    elif (keyPlayed == 80):
        keyType = 1
        xPos = xPos + 636
    elif (keyPlayed == 81):
        keyType = 2
        xPos = xPos + 649
    elif (keyPlayed == 82):
        keyType = 1
        xPos = xPos + 664
    elif (keyPlayed == 83):
        keyType = 3
        xPos = xPos + 667
    elif (keyPlayed == 84):
        keyType = 4
        xPos = xPos + 692

#Octave 5
        
    elif (keyPlayed == 85):
        keyType = 1
        xPos = xPos + 706
    elif (keyPlayed == 86):
        keyType = 2
        xPos = xPos + 721
    elif (keyPlayed == 87):
        keyType = 1
        xPos = xPos + 735
    elif (keyPlayed == 88):
        keyType = 3
        xPos = xPos + 741
    elif (keyPlayed == 89):
        keyType = 4
        xPos = xPos + 765
    elif (keyPlayed == 90):
        keyType = 1
        xPos = xPos + 779
    elif (keyPlayed == 91):
        keyType = 5
        xPos = xPos + 793
    elif (keyPlayed == 92):
        keyType = 1
        xPos = xPos + 808
    elif (keyPlayed == 93):
        keyType = 2
        xPos = xPos + 821
    elif (keyPlayed == 94):
        keyType = 1
        xPos = xPos + 836
    elif (keyPlayed == 95):
        keyType = 3
        xPos = xPos + 839
    elif (keyPlayed == 96):
        keyType = 4
        xPos = xPos + 864

    return (xPos, yPos, keyType)
    
    

myfont = pygame.font.SysFont('Comic Sans MS', 25)

(width, height) = (1000, 800)
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

text = ""

_DEBUG = True;

try:
    #=======DEBUG FOR NO KEYBOARD
    if not _DEBUG:
        inp = pygame.midi.Input(1)
    print ("midi input made")

except pygame.midi.MidiException:
    textsurface = myfont.render("MIDI device input error. Press Enter to close program.", False, WHITE)
    screen.blit(textsurface,(0,0))
    pygame.display.flip()
    #Once "No Device Found" is thrown, it will keep getting thrown even if MIDI input does exist
    while(True): 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    sys.exit()   
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
    #'Device id given is not a valid input id, it is an output id.'
#FUTURE TO-DO: Determine if Midi In and Midi Out are switched, if so inform user

except Exception as exception:
    textsurface = myfont.render("Unknown Exception" +" "+ exception.__class__.__name__, False, WHITE)
    screen.blit(textsurface,(0,0))
    pygame.display.flip()
    #Once "No Device Found" is thrown, it will keep getting thrown even if MIDI input does exist
    while(True): 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    sys.exit()   
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
    
keyOn = False
timer = 0
lastPlayedMidi_value = 0

#Setting up the rhyhm event 
bpm = 164
beatInMs = (60/164)*1000
#Making my own custom Event 
#Using (pygame.USEREVENT+1) because it is a value between USEREVENT and NUMEVENTS
RHYTHM_EVENT = pygame.USEREVENT+1
pygame.time.set_timer(RHYTHM_EVENT, int(beatInMs))

#DEBUG TO SEE IF BEATS WORK
beats = 0
while True:
    clock.tick(60)  
    
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()   
        if evt.type == RHYTHM_EVENT: # is called every 'beatInMs' milliseconds
            beats = beats + 1
            #----TODO:
            #Make this add a line to a downards scrolling canvas above the piano
            

    
    text=""   
    
    #=======DEBUG FOR NO KEYBOARD
    if(_DEBUG):
        midi_value = 50     #debug
        lastPlayedMidi_value = 50
    #36-95
    #If _DEBUG is enabled, inp is undefined.
    #This is okay because "not _DEBUG" will be false and if statment quit
    #before reading the "and inp.poll()"
    if not _DEBUG and inp.poll():
    #if False:
        midi_values = inp.read(1000)   
        midi_value = midi_values[0][0][1]
        screen.fill(BLACK)
        #If a midi event occured AND It is not a Key Off Event
        if(midi_value!=0 and midi_values[0][0][2]!=0):
            keyOn = True
            lastPlayedMidi_value = midi_value
            timer = time.time()
            
            #FUTURE TASKS: Figure out how to detect when Key is On vs Off
            #This way we can highlight it for the correct duration
            #print(str(midi_values[0][0][1]) + " " + str(midi_values[0][0][2]))
            #print(midi_values)
            

    textsurface = myfont.render("PIANO HERO " + str(beats), False, WHITE)
    screen.blit(textsurface,(50 ,700))

    keys = pygame.image.load("AlethaKeyboard.png")
    screen.blit(keys,(50,500))
    
    #=======DEBUG NO KEYBOARD:
    if(keyOn) or _DEBUG:
    #if not keyOn:
        midi_value = lastPlayedMidi_value
        DrawPressedKey(36,50,503,midi_value,screen)
        text =  str(midi_value) + " " + str(number_to_note(midi_value))
        textsurface = myfont.render(text, False, WHITE)
        screen.blit(textsurface,(550,700))
        #=======DEBUG NO KEYBOARD:

        if not _DEBUG and time.time() - 0.3 > timer:
        #if False:
                timer = 0
                keyOn = False
        
    
    
    pygame.display.flip()
    

#/30 + 10
    
        
#if __name__ == '__main__': main()