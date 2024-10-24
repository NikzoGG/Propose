import pygame
import random
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('skibidi_propose')
clock = pygame.time.Clock()

darkbuttonimg = pygame.image.load("assets/darkbutton.png")
lightbuttonimg = pygame.image.load("assets/lightbutton.png")

black = pygame.image.load("assets/Black.png")
black_rect = black.get_rect(topleft=(0, 0))
white = pygame.image.load("assets/white.png")
white_rect = white.get_rect(topleft=(0, 0))

asktext = pygame.image.load("assets/asktext.png")
asktext_rect = asktext.get_rect(topleft=(100,120))

yesbutton = pygame.image.load("assets/yes.png")
yesbutton_rect = yesbutton.get_rect(topleft=(180,150))
nobutton = pygame.image.load("assets/no.png")
nobutton_rect = nobutton.get_rect(topleft=(180,200))

ending = pygame.image.load("assets/ending.png")
ending_rect = ending.get_rect(topleft=(0,0))

ended = False

#random pos picking where the index is a random number which isnt the same as the last one
random_number = random.randint(0,6)
nopositionsy = [400,200,300,100,50,120,440]
last_random_number = random_number

class ThemeButton:
    def __init__(self, x, y, style):
        self.x = x
        self.y = y
        self.style = style
        self.rect = darkbuttonimg.get_rect(topleft=(self.x, self.y))

    def stylechange(self):
        if self.style == 1:
            self.rect = darkbuttonimg.get_rect(topleft=(self.x, self.y))  
            screen.blit(lightbuttonimg, themebutton.rect)  
        elif self.style == 2:
            self.rect = lightbuttonimg.get_rect(topleft=(self.x, self.y))  
            screen.blit(darkbuttonimg, themebutton.rect)  

# Object init
themebutton = ThemeButton(265,0,2)

running = True
while running:
    mousepos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse click check
        if event.type == pygame.MOUSEBUTTONDOWN:
            if themebutton.rect.collidepoint(mousepos):
                if themebutton.style == 1:
                    themebutton.style = 2
                elif themebutton.style == 2:
                    themebutton.style = 1

            if yesbutton_rect.collidepoint(mousepos):
                ended = True

 
    #background color change
    if themebutton.style == 1:
        screen.blit(black, black_rect)
    else:
        screen.blit(white, white_rect)
    
    #mouse hover checkings
    if nobutton_rect.collidepoint(mousepos):
        while random_number == last_random_number:
            random_number = random.randint(0,6)
        print("Pleaseeeeee!!")
        nobutton_rect.y = nopositionsy[random_number]
        last_random_number = random_number
        
        

    #object functions
    themebutton.stylechange()

    screen.blit(asktext,asktext_rect)
    screen.blit(yesbutton,yesbutton_rect)
    screen.blit(nobutton,nobutton_rect)
    #showing ending
    if ended == True:
        screen.blit(ending,ending_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()
