#by: Jorge Kenned Ferreira dos Santos (but call only kenned :) )
#on: 11/01/2022
#-----------------
#-----------
#-----
#-

#imports---------------------------------------------
import math
import thorpy
import pygame

#starting pygame-------------------------------------
pygame.init()
ds = pygame.display.set_mode((480, 480))
#name of app-----------------------------------------
pygame.display.set_caption("Quadratic Bézier Curves")

#constants-------------------------------------------
MOUSE = pygame.mouse
FPS = pygame.time.Clock()
BLACK = (0,0,0)
GRAY = (175,175,175)
WHITE = (255,255,255)

#thorpy constants------------------------------------
n_lines_slider = thorpy.SliderX(50, (5, 30), "Number of lines:", type_=int)
n_line_explain_text = thorpy.OneLineText("Number of lines used to make bézier.")
n_line_curiosity_text = thorpy.OneLineText("The smoothness is proportional to that...")
controls_text = thorpy.OneLineText("CONTROLS:")
r_button_explain_text = thorpy.OneLineText("Press right mouse button to set first point")
l_button_explain_text = thorpy.OneLineText("Press left mouse button to set the another point")

#making box to all gui elements
box = thorpy.Box(elements=[n_lines_slider,
                        n_line_explain_text,
                        n_line_curiosity_text,
                        controls_text,
                        r_button_explain_text,
                        l_button_explain_text])

menu = thorpy.Menu(box)

#variables-------------------------------------------
points = []
n_lines = 10
is_running = True

#default values
x0 = 100
y0 = 450

x2 = 550
y2 = 110

x3 = 650
y3 = 450
#----------------------------------------------------

#seting surface and position of GUI
for element in menu.get_population():
    element.surface = ds
box.set_topleft((10,10))

#main loop
while is_running:
    #paint screen to white (it is like a "clear" screen)
    ds.fill(WHITE)
    #clearing points
    points.clear()

    #make variables from states of pressed mouse buttons
    #i use this because make more simple to use
    left,midle,right = MOUSE.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #quit application
            is_running=False

        #getting position from mouse
        elif right:
            x2,y2 = MOUSE.get_pos()
        elif left:
            x0,y0 = MOUSE.get_pos()

        #set event from thorpy menu
        menu.react(event)

    #getting position 
    x1 = MOUSE.get_pos()[0]
    y1 = MOUSE.get_pos()[1]

    #adding first point to complete the bezier line
    points.append((x0,y0))

    #"calculating" the bezier based in 3 points
    for i in range(n_lines):
        t = i/n_lines

        bx = (math.pow((1 - t),2)*x0 +2 * t*(1-t) * x1 + math.pow(t,2) * x2)
        by = (math.pow((1 - t),2)*y0 +2 * t*(1-t) * y1 + math.pow(t,2) * y2)

        points.append((bx, by))
    points.append((x2,y2))

    
    #drawing lines
    for i in range(0, len(points)):
        if i < len(points)-1:
           pygame.draw.line(ds, BLACK, (points[i]), (points[i+1]),width=1)


    #getting points to gray lines
    #its are make by sum of points divided by 2
    xm0 = (x0+x1)/2
    ym0 = (y0+y1)/2
    xm1 = (x1+x2)/2
    ym1 = (y1+y2)/2

    #drawing gray lines 
    pygame.draw.line(ds, GRAY, (x0,y0), (xm0,ym0), width=1)
    pygame.draw.line(ds, GRAY, (x2,y2), (xm1,ym1), width=1)


    #drawing circles
    pygame.draw.circle(ds, BLACK, (x0,y0),5)
    pygame.draw.circle(ds, BLACK, (x1,y1),3,1, draw_top_left=False)
    pygame.draw.circle(ds, BLACK, (x2,y2),5)

    #get n_lines from slider
    n_lines = n_lines_slider.get_value()

    #"drawing" the GUI
    box.blit()
    box.update()
    
    #updating pygame
    pygame.display.update()


