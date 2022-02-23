# Setup pygame/window ---------------------------------------- #
from asyncio.windows_events import NULL
import pygame
from pygame.locals import *
import sys
import random
import time

pygame.init()

WIDTH, HEIGHT = 680, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))    # set the display mode, window title and FPS clock
pygame.display.set_caption('EARFQUAKE') #Names the window EARFQUAKE
FPSCLOCK = pygame.time.Clock() #Creates a timer called FPSCLOCK
font = pygame.font.SysFont(None, 50)

# the data for the map expressed as [row[tile]].
map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
]
 
#Creates the variables for the tile pngs
endTile = pygame.image.load('Tiles/wall.png').convert_alpha()  # load images
ground = pygame.image.load('Tiles/CoolTile.png').convert_alpha()
player_img = pygame.transform.scale(pygame.image.load('Tiles/PlayerSprite.png').convert_alpha(), (32,32))

#Sets the tile hiehgt and width
tilewidth = tileheight = 64  # holds the tile width and height
halfTileHeight = tileheight /2
halfTileWidth = tilewidth /2

#Creates the variables to play soundfx and music
blockFallingSound = pygame.mixer.Sound('Sounds/BlockFalling.wav')
gameOverSound = pygame.mixer.Sound('Sounds/GameOver.wav')
gameOverSound.set_volume(.6)
playerMovementSound = pygame.mixer.Sound('Sounds/PlayerMovement.wav')

#Sets menu music
pygame.mixer.music.load('Sounds/MenuMusic.mp3')
pygame.mixer.music.play(-1)

#Function to draw text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#Main menu funcion
def main_menu():
    while True:
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        win.fill((250,175,216))
        draw_text('EARFQUAKE', font, (0,0,0), win, 50, 50)
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(50, 100, 200, 50)
        if button_1.collidepoint((mx, my)) and click:
            world.__init__(map_data)
            player.__init__(world)
            game()
        pygame.draw.rect(win, (255,255,255), button_1)
        draw_text('Play', font, (0,0,0), win, 50, 100)
        click = False
 
        pygame.display.update()
        FPSCLOCK.tick(60)


 
def game():
    while True:
        for event in pygame.event.get():
            # Game closes/ends when the user presses the ESCAPE key or presses the X button on the window
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    main_menu()
                # Movement
                if event.key == pygame.K_LEFT:
                    player.left_pressed = True
                if event.key == pygame.K_RIGHT:
                    player.right_pressed = True
                if event.key == pygame.K_UP:
                    player.up_pressed = True
                if event.key == pygame.K_DOWN:
                    player.down_pressed = True
        player.update() #updates the player so the player can move and do other functions
        pygame.display.flip() #Takes anything that is drawn in the main loop it draws it on the screen
        FPSCLOCK.tick(120) # Keeps framerate at 120 FPS

def gameOverScreen():
    
    while True:
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                click = True
 
        win.fill((250,175,216))
        draw_text('GAME OVER', font, (0,0,0), win, 50, 50)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)) and click:
                main_menu()
        if button_2.collidepoint((mx, my)) and click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(win, (255, 255, 255), button_1)
        pygame.draw.rect(win, (255, 255, 255), button_2)
        draw_text('Play Again', font, (0,0,0), win, 50, 100)
        draw_text('Quit', font, (0,0,0), win, 50, 200)
        click = False
 
        pygame.display.update()
        FPSCLOCK.tick(60)
        
def winScreen():
    
    while True:
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                click = True
 
        win.fill((250,175,216))
        draw_text('You win!', font, (0,0,0), win, 50, 50)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)) and click:
                main_menu()
        if button_2.collidepoint((mx, my)) and click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(win, (255, 255, 255), button_1)
        pygame.draw.rect(win, (255, 255, 255), button_2)
        draw_text('Play Again', font, (0,0,0), win, 50, 100)
        draw_text('Quit', font, (0,0,0), win, 50, 200)
        click = False
 
        pygame.display.update()
        FPSCLOCK.tick(60)

class World():
    def __init__(self, data):
        self.tileList = data
        self.tileGroup = pygame.sprite.Group()
        for rownumber, row in enumerate(data):
            for columnnumber, tile in enumerate(row):
                if columnnumber == 9 and rownumber == 9:
                    tileImage = endTile
                else:
                    tileImage = ground

                # Math for proper tile placement and draws tiles
                cartesianX = rownumber * halfTileWidth  
                cartesianY = columnnumber * halfTileHeight
                isometricX = (cartesianX - cartesianY) 
                isometricY = (cartesianX + cartesianY)/2
                centeredX = win.get_rect().centerx + isometricX
                centeredY = win.get_rect().centery/2 + isometricY


                tileCollisionBox = pygame.sprite.Sprite()
                tileCollisionBox.image = pygame.Surface((75, 75))
                tileCollisionBox.image.fill((255, 0, 0))
                tileCollisionBox.rect = pygame.Rect(*win.get_rect().center, 10, 10)        
                tileCollisionBox.rect.center = (centeredX + 32, centeredY + 16)


                isInVision = False
                self.tileList[rownumber][columnnumber] = [tileImage, centeredX, centeredY, tileCollisionBox, 0, 10, isInVision]
                
                win.blit(tileImage, (centeredX, centeredY))
                pygame.draw.rect(win, (0, 255, 0), tileCollisionBox.rect)
        
        for row in self.tileList:
            for tile in row:
                self.tileGroup.add(tile[3])
    
    def draw(self):
        for row in self.tileList:
            for tile in row:
                if tile[4] == 1:
                    win.blit(tile[0], (tile[1] + (player.Xmovement - player.Ymovement), tile[2] + ((player.Xmovement + player.Ymovement)/2) + tile[5]))
                    tile[5] += 2
                    if tile[5] > 1000:
                        tile[4] += 1
                if tile[4] == 0 or tile[0] == endTile:
                    win.blit(tile[0], (tile[1] + (player.Xmovement - player.Ymovement), tile[2] + ((player.Xmovement + player.Ymovement)/2)))
                    tile[3].rect.center = (tile[1] + (player.Xmovement - player.Ymovement) + 32, tile[2] + ((player.Xmovement + player.Ymovement)/2) + 16)

                if pygame.sprite.spritecollide(tile[3], player.playerVisionGroup, False, pygame.sprite.collide_circle):
                    tile[6] = True
                else:
                    tile[6] = False
                

        win.fill((250,175,216))

        for row in self.tileList:
            for tile in row:
                #Tile falls animation
                if tile[4] == 1:
                    win.blit(tile[0], (tile[1] + (player.Xmovement - player.Ymovement), tile[2] + ((player.Xmovement + player.Ymovement)/2) + tile[5]))
                    tile[3].rect.center = (tile[1] + (player.Xmovement - player.Ymovement), tile[2] + ((player.Xmovement + player.Ymovement)/2) + tile[5])
                    tile[5] += 2
                    if tile[5] > 1000:
                        tile[4] += 1
                #Tile spawns if in the vision
                if (tile[4] == 0 and tile[6]) or tile[0] == endTile:
                    win.blit(tile[0], (tile[1] + (player.Xmovement - player.Ymovement), tile[2] + ((player.Xmovement + player.Ymovement)/2)))
                    tile[3].rect.center = (tile[1] + (player.Xmovement - player.Ymovement) + 32, tile[2] + ((player.Xmovement + player.Ymovement)/2) + 16)

world = World(map_data)

#Player Class
class Player:
    def __init__(self, world):
        self.moveCount = 0
        self.x = world.tileList[0][0][1] + halfTileWidth/2
        self.y = world.tileList[0][0][2] - halfTileWidth/4
        self.screenPosition = (self.x, self.y)

        self.collisionBox = pygame.sprite.Sprite()
        self.collisionBox.image = pygame.Surface((75, 75))
        self.collisionBox.image.fill((255, 0, 0))
        self.collisionBox.rect = pygame.Rect(*win.get_rect().center, 15, 15)        
        self.collisionBox.rect.center = (self.x + 16, self.y + 16)

        self.Xmovement = 0
        self.Ymovement = 0
        self.playerFall = 10
        self.activateTile = False
        self.location = [0,0]
        self.onatile = True

        self.playerVision = pygame.sprite.Sprite()
        self.playerVision.image = pygame.Surface((80, 80), pygame.SRCALPHA)
        pygame.draw.circle(self.playerVision.image, (100, 0, 0), (40, 40), 40)
        self.playerVision.rect = pygame.Rect(*win.get_rect().center, 100, 100)
        self.playerVision.rect.center = (self.x + 16, self.y + 16) 
        self.playerVisionGroup = pygame.sprite.Group(self.playerVision)

        self.playerDead = False

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        win.blit(player_img, self.screenPosition)

    def onAnyTile(self):
        if not pygame.sprite.spritecollide(self.collisionBox, world.tileGroup, False) or self.playerDead:
            if self.playerFall == 15:
                gameOverSound.play()
            self.playerDead = True
            if (self.playerFall > 1000):
                gameOverScreen()
        
        elif pygame.Rect.colliderect(self.collisionBox.rect, world.tileList[9][9][3].rect):
            winScreen()
        
    def update(self):
        #Checks player movement
        if (self.playerDead == False):
            if self.left_pressed and not self.right_pressed and not self.down_pressed and not self.up_pressed:
                playerMovementSound.play()
                self.Xmovement += halfTileWidth
                self.activateTile = True
            if self.right_pressed and not self.left_pressed and not self.down_pressed and not self.up_pressed:
                playerMovementSound.play()
                self.Xmovement -= halfTileWidth
                self.activateTile = True
            if self.up_pressed and not self.down_pressed and not self.right_pressed and not self.left_pressed:
                playerMovementSound.play()
                self.Ymovement += halfTileHeight
                self.activateTile = True
            if self.down_pressed and not self.up_pressed and not self.right_pressed and not self.left_pressed:
                playerMovementSound.play()
                self.Ymovement -= halfTileHeight
                self.activateTile = True
        
        #Randomly removes tiles every 2 player movements
        randomRow = random.choice(world.tileList)
        randomTileIndex =  random.randint(0,len(randomRow)-1)

        if self.activateTile and not randomRow[randomTileIndex][0] == endTile: #randomly deletes tiles
            blockFallingSound.play()
            randomRow[randomTileIndex][4] += 1
            self.activateTile = False


        win.fill((0,0,0))

        world.draw()

        if (self.playerDead == False):
            win.blit(player_img, (self.x, self.y))
        else:
            self.collisionBox.rect.center = (self.x + 16, self.y + 16 + self.playerFall)
            win.blit(player_img, (self.x, self.y + self.playerFall))
            self.playerFall += 5
    
        player.left_pressed = False
        player.right_pressed = False
        player.up_pressed = False
        player.down_pressed = False
        self.onAnyTile()

player = Player(world)
 
main_menu()