import pygame
from random import randint
import os
import socketio
import threading

pygame.init()
pygame.font.init()

SCREEN = pygame.display.set_mode((500, 750))

Background_image = pygame.image.load('Flappy Fitness\\background.jpg')
bird_image = pygame.image.load('Flappy Fitness\\bird1.png')
squats_img = pygame.image.load('Flappy Fitness\\squat.png')
jumpingjacks_img = pygame.image.load('Flappy Fitness\\jumping jack.png')
toetouches_img = pygame.image.load('Flappy Fitness\\toe touch.png')

sio = socketio.Client()
did_user_jumped = False

fg_color = (255,255,255)

color_light = (146, 183, 247)
color_dark = (112, 139, 186)

width = SCREEN.get_width()
height = SCREEN.get_height()

smallfont = pygame.font.SysFont('Corbel', 35)
smallfont2 = pygame.font.SysFont('Corbel', 26)
play_text = smallfont.render('Play', True, fg_color)
instructions_text = smallfont.render('Instructions', True, fg_color)
back_text = smallfont.render('Back', True, fg_color)
squat_text = smallfont2.render('Squat', True, fg_color)
jumpingjack_text = smallfont2.render('Jumping Jack', True, fg_color)
toetouch_text = smallfont2.render('Toe Touch', True, fg_color)

squats_img = pygame.image.load('Flappy Fitness\\squat.png')
jumpingjacks_img = pygame.image.load('Flappy Fitness\\jumping jack.png')
toetouches_img = pygame.image.load('Flappy Fitness\\toe touch.png')

def connect_to_server():
    sio.connect('http://localhost:8000')
    sio.wait()

@sio.event
def connect():
    print('Game connected to server')
    # run_game()

@sio.event
def disconnect():
    print('Disconnected from server')
    pygame.quit()


@sio.event
def flappy_bird_move(data):
    global did_user_jumped
    print("USER JUMPED")
    did_user_jumped = True
    

# connect_to_server()

threading.Thread(target=connect_to_server).start()

bird_x = 50
bird_y = 300
bird_y_change = 0
bird_y_change_factor = 1

def display_bird(bird_image, bird_x, bird_y):
    SCREEN.blit(bird_image, (bird_x, bird_y))

obstacle_width = 70
obstacle_height = randint(450, 600)
obstacle_color = (211, 253, 117)
obstacle_x_change_factor = 0.7
obstacle_x_change = -1
obstacle_x = 500

def display_obstacle(object_height, y_pos):
    pygame.draw.rect(SCREEN, obstacle_color, (obstacle_x, y_pos, obstacle_width, object_height))

def collision_detection(obstacle_x, obstacle_height, bird_y, bottom_obstacle_height):
    if obstacle_x >= 50 and obstacle_x <= (50 + 64):
        if bird_y <= obstacle_height or bird_y >= (bottom_obstacle_height - 64):
            return True
        return False

score = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)

def score_display(score):
    display = score_font.render(f"score {score}", True, (255,255,255))
    SCREEN.blit(display, (10, 10))

def instructions():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (width / 2 - 70) <= mouse[0] <= (width / 2 + 70) and (int(height / 3 * 2 + 50)) <= mouse[1] <= (int(height / 3 * 2 + 90)):
                    run = False
        
        SCREEN.fill((102, 111, 189))

        mouse = pygame.mouse.get_pos()

        SCREEN.blit(toetouches_img, (12, int(height / 2 - 135)))
        SCREEN.blit(jumpingjacks_img, (175, int(height / 2 - 69)))
        SCREEN.blit(squats_img, (338, int(height / 2 - 84)))

        SCREEN.blit(toetouch_text, (32, int(height / 2 - 165)))
        SCREEN.blit(jumpingjack_text, (182, int(height / 2 - 99)))
        SCREEN.blit(squat_text, (378, int(height / 2 - 114)))

        if (width / 2 - 70) <= mouse[0] <= (width / 2 + 70) and (int(height / 3 * 2 + 50)) <= mouse[1] <= (int(height / 3 * 2 + 90)):
            pygame.draw.rect(SCREEN, color_light, [width / 2 - 70, int(height / 3 * 2 + 50), 140, 40])
        else:
            pygame.draw.rect(SCREEN, color_dark, [width / 2 - 70, int(height / 3 * 2 + 50), 140, 40])
        
        SCREEN.blit(back_text, (width / 2 - 30, int(height / 3 * 2 + 53)))
        pygame.display.update()

running = True

started = False
clock = pygame.time.Clock()
while running:

    SCREEN.fill((0, 0, 0))

    SCREEN.blit(Background_image, (0, 0))
    if not started:
        start = score_font.render('', True, (255,255,255))

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (width / 2 - 70) <= mouse[0] <= (width / 2 + 70) and (int(height / 3 * 2)) <= mouse[1] <= (int(height / 3 * 2 + 40)):
                    started = True
                
                if (width / 2 - 90) <= mouse[0] <= (width / 2 + 90) and (int(height / 3 * 2 + 50)) <= mouse[1] <= (int(height / 3 * 2 + 90)):
                    instructions()

        if (width / 2 - 70) <= mouse[0] <= (width / 2 + 70) and (int(height / 3 * 2)) <= mouse[1] <= (int(height / 3 * 2 + 40)):
            pygame.draw.rect(SCREEN, color_light, [width / 2 - 70, int(height / 3 * 2), 140, 40])
        else:
            pygame.draw.rect(SCREEN, color_dark, [width / 2 - 70, int(height / 3 * 2), 140, 40])
        
        if (width / 2 - 70) <= mouse[0] <= (width / 2 + 70) and (int(height / 3 * 2 + 50)) <= mouse[1] <= (int(height / 3 * 2 + 90)):
            pygame.draw.rect(SCREEN, color_light, [width / 2 - 90, int(height / 3 * 2 + 50), 180, 40])
        else:
            pygame.draw.rect(SCREEN, color_dark, [width / 2 - 90, int(height / 3 * 2 + 50), 180, 40])
        
        SCREEN.blit(instructions_text, (width / 2 - 80, int(height / 3 * 2 + 53)))

        SCREEN.blit(play_text, (width / 2 - 30, int(height / 3 * 2 + 3)))

        SCREEN.blit(start, (0, 0))

    jumped = False
    for event in pygame.event.get():
        print(did_user_jumped)
        if event.type == pygame.QUIT:
            running = False
    if did_user_jumped:
        print("JUMP found")
        bird_y_change = -4.55
        print(bird_y)
        did_user_jumped = False
        print(True)

    if started:
        bird_y_change += 0.15
        bird_y_change = min(bird_y_change, 0.8)
        bird_y += bird_y_change

        if bird_y <= 0:
            bird_y = 0
        if bird_y > 571:
            bird_y = 571

        obstacle_x += obstacle_x_change*obstacle_x_change_factor
        if obstacle_x <= -10:
            obstacle_x = 500
            obstacle_height = randint(200, 400)
            score += 1 

        collision = collision_detection(obstacle_x, obstacle_height, bird_y, obstacle_height + 150)

        if collision:
            pygame.quit()
        
        obstacle_x_change_factor += 0.0015

    bottom_obstacle_height = 635 - obstacle_height - 150
    display_obstacle(obstacle_height, 0)
    display_obstacle(bottom_obstacle_height, obstacle_height + 150)
    display_bird(bird_image, bird_x, bird_y)


    score_display(score)

    pygame.display.update()

    clock.tick(60)

pygame.quit()