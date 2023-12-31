import pygame
import os

WIDTH,HEIGHT=900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Shooter Game")
WHITE=(255,255,255)

BORDER=pygame.Rect(WIDTH/2-5,0,10,HEIGHT)

FPS=60
velocity=5
bullet_velocity=7
MAX_BULLETS=3
SPACESHIP_WIDTH,SPACESHIP_HEIGHT=55,40

YELLOW_SPACESHIP=pygame.image.load("Assets\spaceship_yellow.png")
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

RED_SPACESHIP=pygame.image.load("Assets\spaceship_red.png")
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

def draw_window(red,yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN,"black",BORDER)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    pygame.display.update()
def yellow_handle_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a]:
            yellow.x-=velocity
    if keys_pressed[pygame.K_d]:
            yellow.x+=velocity
    if keys_pressed[pygame.K_w]:
            yellow.y-=velocity
    if keys_pressed[pygame.K_s]:
            yellow.y+=velocity
def red_handle_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT]:
            red.x-=velocity
    if keys_pressed[pygame.K_RIGHT]:
            red.x+=velocity
    if keys_pressed[pygame.K_UP]:
            red.y-=velocity
    if keys_pressed[pygame.K_DOWN]:
            red.y+=velocity
def onscreen(red,yellow):
    if red.x>=860:
        red.x=860
    if red.x<=455:
        red.x=455
    if red.y>=450:
        red.y=450
    if red.y<=0:
        red.y=0
    if red.x<=455:
        red.x=455
    if yellow.x<=0:
            yellow.x=0
    if yellow.x>=405:
            yellow.x=405
    if yellow.y>=450:
        yellow.y=450
    if yellow.y<=0:
        yellow.y=0
def handle_bullets(yellow_bullets,red_bullets,yellow,red):
     for bullet in yellow_bullets:
        bullet.x+=bullet_velocity
        if yellow.colliderect(bullet):
            yellow_bullets.remove(bullet)      

def main():
    red=pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow=pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
 
    red_bullets=[]
    yellow_bullets=[]

    clock= pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LCTRL and len(yellow_bullets)<MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height/2-2,10,5)
                    yellow_bullets.append(bullet)
                if event.key==pygame.K_RCTRL and len(red_bullets)<MAX_BULLETS:
                    bullet = pygame.Rect(red.x,red.y+red.height/2-2,10,5)
                    red_bullets.append(bullet)
        print(red_bullets,yellow_bullets)             
        keys_pressed=pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)
        onscreen(red,yellow)
        handle_bullets(yellow_bullets,red_bullets,yellow,red)



        draw_window(red,yellow)
        
    pygame.quit()


if __name__=="__main__":
    main()


