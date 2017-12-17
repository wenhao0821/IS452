import pygame,sys,time,random
from pygame.locals import *
# define the color used in this case
red = pygame.Color(255, 0, 0)  # red color
black = pygame.Color(0, 0, 0)  # black color
white = pygame.Color(255, 255, 255)  # white color
blue = pygame.Color(0, 0, 200)  # blue color

# define the function of die
def die(playSurface,score):
    channel=pygame.mixer.Channel(3)
    sound2=pygame.mixer.Sound('die.wav')
    channel.play(sound2)
    dieFont = pygame.font.SysFont('Arial', 30)  # define the font size and type
    dietext = dieFont.render('You Lose! The score you get is: ' + str(score), True, red)
    pygame.mixer.music.stop()
    dieRect = dietext.get_rect()
    dieRect.midtop= (200, 200)
    playSurface.blit(dietext, dieRect)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()  # quit the module
    sys.exit()  # exit the system

# define the main function
def main():
    # initialize the pygame
    pygame.init()
    pygame.mixer.music.load('snackmusic.mp3')  # 加载mp3
    pygame.mixer.music.play(-1)
    channel=pygame.mixer.Channel(2)
    sound=pygame.mixer.Sound('get.wav')
    fpsClock = pygame.time.Clock()
    # create the surface of the pygame
    playSurface = pygame.display.set_mode((640,480))
    pygame.display.set_caption('The Snake Game')

    # initialize the variables
    score=0
    snakePos = [320,240]
    snake = [[320,240],[310,240],[300,240]]
    candypos = [200,200]
    candy = 1
    currentorder = 'right'
    nextorder = currentorder
    while True:
        # listen to pygame events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # listen to keyboard events
                if event.key == K_RIGHT :
                    nextorder = 'right'
                if event.key == K_LEFT :
                    nextorder = 'left'
                if event.key == K_UP :
                    nextorder = 'up'
                if event.key == K_DOWN :
                    nextorder = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        # determine whether the typed direction is correct
        if nextorder == 'right' and  currentorder != 'left':
            currentorder = nextorder
        if nextorder == 'left' and  currentorder != 'right':
            currentorder = nextorder
        if nextorder == 'up' and currentorder != 'down':
            currentorder = nextorder
        if nextorder == 'down' and currentorder != 'up':
            currentorder = nextorder
        # change the snack head's coordinates based on the direction
        if currentorder == 'right':
            snakePos[0] += 10
        if currentorder == 'left':
            snakePos[0] -= 10
        if currentorder == 'up':
            snakePos[1] -= 10
        if currentorder == 'down':
            snakePos[1] += 10
        # add the length of snack
        snake.insert(0,list(snakePos))
        # determine whether the snack eat the candy
        if snakePos[0] == candypos[0] and snakePos[1] == candypos[1]:
            candy = 0
            score= score+1
            channel.play(sound)
        else:
            snake.pop()
        # if snack eats the candy, generate a new candy in a random position
        if candy == 0:
            x = random.randrange(1,64)
            y = random.randrange(1,48)
            candypos = [int(x*10),int(y*10)]
            candy = 1
        # draw the pygame surface
        playSurface.fill(white)
        for position in snake:
            pygame.draw.rect(playSurface, blue, Rect(position[0], position[1], 10, 10))
            pygame.draw.rect(playSurface, black, Rect(candypos[0], candypos[1], 10, 10))

        # refresh the pygame surface
        pygame.display.flip()
        # determine whether snack is dead
        if snakePos[0] > 630 or snakePos[0] < 0:
            die(playSurface,score)
        if snakePos[1] > 470 or snakePos[1] < 0:
            die(playSurface,score)
        for snakeBody in snake[1:]:
            if snakePos[0] == snakeBody[0] and snakePos[1] == snakeBody[1]:
                die(playSurface,score)

        # control the game speed
        fpsClock.tick(10)

if __name__ == "__main__":
    main()
