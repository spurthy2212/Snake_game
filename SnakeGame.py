import pygame
import random
import os

pygame.init()

width,height = 600,600
game_screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")

snake_x,snake_y = width/2,height/2
change_x,change_y = 0,0

food_x,food_y = random.randrange(0,width)//10*10,random.randrange(0,height)//10*10

clock=pygame.time.Clock()
snake_body = [(snake_x,snake_y)]

score=0

high_score = 0
high_score_file = "high_score.txt"

if os.path.exists(high_score_file):
    with open(high_score_file, "r") as file:
        high_score = int(file.read())

font = pygame.font.SysFont("Arial", 24)
game_over_font = pygame.font.SysFont("Arial", 50)
final_score_font = pygame.font.SysFont("Arial", 30)
game_over = False

def display_score():
    score_text = font.render(f"Score: {score}", True, (255, 255, 0))  # Yellow color
    game_screen.blit(score_text, [10, 10])
    high_score_text = font.render(f"High Score: {high_score}", True, (0, 255, 255))  # Cyan
    game_screen.blit(high_score_text, [10, 40])

def display_game_over():
    text = game_over_font.render("GAME OVER", True, (255, 0, 0))  # Red
    game_screen.blit(text, [width // 2 - 140, height // 2 - 50])

    score_text = final_score_font.render(f"Final Score: {score}", True, (255, 255, 0))  # Yellow
    game_screen.blit(score_text, [width // 2 - 100, height // 2 + 10])

def display_snake_food():
    global snake_x,snake_y,food_x,food_y,score,game_over
    if not game_over:
        snake_x = (snake_x + change_x)%width
        snake_y = (snake_y + change_y)%height

        if((snake_x,snake_y) in snake_body[1:]):
           game_over = True
           if score > high_score:
                high_score = score
                with open(high_score_file, "w") as file:
                    file.write(str(high_score))
           return

    snake_body.append((snake_x,snake_y))

    if(food_x == snake_x and food_y == snake_y):
        score+=1
        food_x,food_y = random.randrange(0,width)//10*10,random.randrange(0,height)//10*10
    else:
        del snake_body[0]

    game_screen.fill((0,0,0))
    pygame.draw.rect(game_screen,(0,255,0),[food_x,food_y,10,10])
    for(x,y) in snake_body:
        pygame.draw.rect(game_screen,(255,255,255),[x,y,10,10])
        display_score()
        if game_over:
           display_game_over()
        pygame.display.update()

while True:
    events = pygame.event.get()
    for event in events:
        if(event.type == pygame.QUIT):
            pygame.quit()
            quit()
        if(event.type == pygame.KEYDOWN):
            if(event.key ==pygame.K_LEFT):
                change_x=-10
                change_y=0
            elif(event.key == pygame.K_RIGHT):
                change_x=10
                change_y=0
            elif(event.key == pygame.K_UP):
                change_x=0
                change_y=-10
            elif(event.key == pygame.K_DOWN):
                change_x=0
                change_y=10

    display_snake_food()
    clock.tick(12)