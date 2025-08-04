#Platformer demo for Yr11
#Juergen Lier
#Version 1_5
#Added button & test on button
#Aug 2023

import pygame
from pygame import image as img
import sys

pygame.init()

# Adding new content
# This is the content added for the second commit...

#Setting the size of the display window
screen_size = ((500, 500))
win = pygame.display.set_mode((screen_size))

ScreenWidth = 500

#Setting a caption for the game
pygame.display.set_caption("Demo platformer")

#importing images
walkRight = [img.load("images/R1.png"), img.load("/images/R2.png"), img.load("images/R3.png"),img.load("images/R4.png"),img.load("images/R5.png"),img.load("images/R6.png"),img.load("images/R7.png"),img.load("images/R8.png"),img.load("images/R9.png")]
walkLeft = [img.load("images/L1.png"), img.load("images/L2.png"), img.load("images/L3.png"),img.load("images/L4.png"),img.load("images/L5.png"),img.load("images/L6.png"),img.load("images/L7.png"),img.load("images/L8.png"),img.load("images/L9.png")]
bg = img.load("images/bg.jpg")
char = img.load("images/standing.png")

clock = pygame.time.Clock()

#Colours
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
blue = (0,0,128)

#Set velocity to control speed of sprite
vel = 5

#Jump code
isJump = False
jumpCount = 10

#Keeping track of how many steps the character has moved. Important so that we know what 
#pic or frame we are moving on.
left = False
right = False
walkCount = 0

#Set co-ordinates of where sprite1 will appear and its height and width
x = 50
y = 417
sprite_width = 64
sprite_height = 64

# stores the width and height of the
# screen into a variable
width = win.get_width()
height = win.get_height()


def buttonExit():
    #Setting the light shade of the button
    button_light = (170,170,170)

    #Setting the dark shade of the button
    button_dark = (100,100,100)

    # create a font object.
    # 1st parameter is the font file which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.SysFont('Corbel.ttf', 32)

    # create a text surface object,on which text is drawn on it.
    #1st parameter is text
    #2nd parameter is setting renter to True so that it shows up
    #3rd parameter is setting font colour
    #4th parameter sets background/highlight of the colour (if needed)
    text = font.render('Quit', True, white)

    # create a rectangular object for the text surface object
    textRect = text.get_rect()
    # set the center of the rectangular object.
    textRect.center = (width // 2+70, height // 2+20)

    # stores the (x,y) coordinates into the variable as a tuple
    mouse = pygame.mouse.get_pos()
    print(mouse[0])
    
    
    #checks if a mouse is clicked
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            pygame.quit()
        #if the mouse is clicked on the
        # button the game is terminated
        #if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
            #pygame.quit()

    # if mouse is hovered on the button it changes to a lighter shade
    # else the button has a dark shade 
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(win,button_light,[width/2,height/2,140,40])
    
    else:
        pygame.draw.rect(win,button_dark,[width/2,height/2,140,40])

    # copying the text surface object to the display surface object
    # at the center coordinate.
    win.blit(text, textRect)

#Game window1
def redrawGameWindow():
    global walkCount
    
    #Insert the background pic. (0,0) is the position where the image will load
    win.blit(bg, (0,0))

    #insert the character in the game
    if walkCount + 1 >= 27:
        walkCount = 0

    if left: # if we are facing left
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right: # if we are facing right
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))  # If the character is standing still
        walkCount = 0
    
    

#Game loop starts
done = True
while done:
    #fps set to 27 cause we only have 27 characters
    clock.tick(60)

    #Quit the game when the window gets closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    
    #Movement code
    #moves character for as long as the key get held down in what ever direction
    #Set up a list to do this.
    #To create boundary so character doesnt move off screen, add 'and' onto key press
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < ScreenWidth - sprite_width - vel:
        x += vel
        left = False
        right = True

    else:
        right = False
        left = False
        walkCount = 0

    #Jump code
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    #Game quits when I press the escape key
    if keys[pygame.K_ESCAPE]:
        done = False
  
    
    redrawGameWindow()
    buttonExit()
    

    #pygame.display.update()

    pygame.display.flip()


pygame.quit()
quit()

