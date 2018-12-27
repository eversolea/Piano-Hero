import pygame as pg, pygame.midi 

WIDTH = 800
HEIGHT = 600
FPS = 60

BLACK = (0,0,0)
BLUE = (0,0,255)


pg.init()
pg.midi.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('STACKOVERFLOW_EXAMPLE_MIDI')
clock = pg.time.Clock()

running = True

inp = pg.midi.Input(1)

x = WIDTH//2
y = HEIGHT//2
speedx = 0

midi_list = []

while running:
    clock.tick(FPS)
    if inp.poll():
        midi_value = inp.read(1000)[0][0][1]
        if midi_value==57:
            midi_list.append(midi_value)
            if len(midi_list)==1:
                speedx = -1
            else:
                speedx = 0
                midi_list = []
        if midi_value == 63:
            running = False
    x = x+speedx
    screen.fill(BLUE)
    pg.draw.rect(screen,BLACK,[x,y,50,60])
    pg.display.update()
    pg.display.flip()

pg.quit()