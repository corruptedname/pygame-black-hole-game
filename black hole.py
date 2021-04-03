import subprocess, sys, os, ctypes
os.system('pip install pathlib --quiet')
from pathlib import Path
os.system('attrib -h check_if_resources_exist.data')
my_file = Path('check_if_resources_exist.data')
if not my_file.is_file():
    print('installing resources')
    subprocess.check_call([sys.executable, '-m', 'pip', '--quiet', 'install',
     '-r', 'requirements.txt'])
    subprocess.check_call([sys.executable, '-m', 'pip', '--quiet', 'install',
     'win32gui'])
    subprocess.check_call([sys.executable, '-m', 'pip', '--quiet', 'install',
     'playsound'])
    os.system('echo. > check_if_resources_exist.data')
    os.system('attrib +h check_if_resources_exist.data')
os.system('attrib +h check_if_resources_exist.data')
from playsound import playsound
import winsound, pygame
from typing import Tuple
import random, time
from random import randint
from linereader import copen
import win32gui
import win32.lib.win32con as win32con
ranx = random.randrange(0, 1000, 10)
rany = random.randrange(0, 380, 10)
worldx = 1000
worldy = 625
fps = 100
ani = 4
pygame.display.set_caption('black hole')
programIcon = pygame.image.load('resources/cube.png')
pygame.display.set_icon(programIcon)
world = pygame.display.set_mode([worldx, worldy])
BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

class Player(pygame.sprite.Sprite):
    __doc__ = '\n    Spawn a player\n    '

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load('resources/cube.png').convert_alpha()
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def render(self):
        window.blit(self.Player, self.rect)

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y


class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        for i in range(1, 6):
            img = pygame.image.load('resources/Ball.png').convert_alpha()
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()


backdrop = pygame.image.load('resources/bg.png')
clock = pygame.time.Clock()
pygame.init()
myfont = pygame.font.SysFont('Chopsic.ttf', 64)
backdropbox = world.get_rect()
main = True
player = Player()
ball = Ball()
player.rect.x = 0
player.rect.y = 0
ball.rect.x = 100
ball.rect.y = 100
ball_list = pygame.sprite.Group()
ball_list.add(ball)
player_list = pygame.sprite.Group()
player_list.add(player)
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
pygame.mixer.init()
pygame.mixer.music.load('resources/deep space.mp3')
pygame.mixer.music.play()
steps = 10
score = 0
while main:
    ranx = random.randrange(0, 630, 10)
    rany = random.randrange(0, 470, 10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        elif event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False

            if event.key == pygame.K_LEFT or (event.key == ord('a')):
                player.rect.x = player.rect.x - 10
                print('x')
                print(player.rect.x)
            if event.key == pygame.K_RIGHT or (event.key == ord('d')):
                player.rect.x = player.rect.x + 10
                print('x')
                print(player.rect.x)
            if event.key == pygame.K_UP or (event.key == ord('w')):
                player.rect.y = player.rect.y - 10
                print('y')
                print(player.rect.y)
            if event.key == pygame.K_DOWN or (event.key == ord('s')):
                player.rect.y = player.rect.y + 10
                print('y')
                print(player.rect.y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            else:
                if event.key == pygame.K_RIGHT or (event.key == ord('d')):
                    player.control(-steps, 0)
                if player.rect.y <= -10:
                    player.rect.y = 0
                if player.rect.x <= -10:
                    player.rect.x = 0
                if player.rect.y >= 630:
                    player.rect.y = 620
                if player.rect.x >= 1010:
                    player.rect.x = 1000
            if player.rect.x == ball.rect.x:
                if player.rect.y == ball.rect.y:
                    ball.kill()
                    ball.rect.x = ranx
                    ball.rect.y = rany
                    ball_list = pygame.sprite.Group()
                    ball_list.add(ball)
                    ball.update()
                    ball_list.draw(world)
                    playsound('resources/pickup1.wav')

    world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(world)
    ball.update()
    ball_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)