# Eric Lu

import pygame
import sys
import time
import random

class BreakoutApp:

    def __init__(self):

        self.x = 200
        self.y = 200
        self.block = []
        self.delta_x =(-1)**(random.randint(1, 2))*random.randint(2,6)
        self.delta_y = random.randint(2,6)
        self.wait = False
        self.first_start = True
        
        for x in range(0, 8):
            new = []
            for y in range(0, 10):
                new.append(1)
            self.block.append(new)
        
        pygame.init()
        self.screen = pygame.display.set_mode((600, 500))
        pygame.display.set_caption('Breakout - Eric Lu')

        pygame.mixer.music.load('background.mp3')
        pygame.mixer.music.play(-1)

    def reset(self):
        
        self.x = 250
        self.y = 250
        self.delta_x =(-1)**(random.randint(1, 2))*random.randint(2,6)
        self.delta_y = random.randint(2,6)
            
    def drawBall(self):

        if (self.x >= 599 or self.x <= 0):
            self.delta_x = -self.delta_x

        if (self.y <= 0):
            self.delta_y = -self.delta_y
            
        self.x += self.delta_x
        self.y += self.delta_y

        pygame.draw.circle(self.screen, (255, 255, 255), (self.x, self.y), 3, 2)
        
    def drawTopBlock(self):

        for x in range(0, len(self.block), 1):
            for y in range(0, len(self.block[x]), 1):

                if (self.block[x][y] == 1):
                    
                    if (x == 0 or x == 1):
                        color = (255, 69, 0) # Red-Orange
                    if (x == 2 or x == 3):
                        color = (255, 255, 0) # Yellow
                    if (x == 4 or x == 5):
                        color = (0, 255, 125) # Green
                    if (x == 6 or x == 7):
                        color = (30, 0, 205) # Blue
                            
                    x_coord = 2 + 60*y
                    y_coord = 35 + 20*x
                    pygame.draw.rect(self.screen, color, pygame.Rect(x_coord, y_coord, 55, 15))

    def testTopCollision(self):

        for x in range(0, len(self.block), 1):
            for y in range(0, len(self.block[x]), 1):

                # (x, y)
                # (2+60*y,35+20*x)     (2+60*y+55,35+20*x)
                #        +-----------------------+
                #        |                       |
                #        |                       |
                #        +-----------------------+
                # (2+60*y,35+20*x+15)  (2+60*y+55,35+20*x+15)
                
                if (self.block[x][y] == 1):
                    if (self.x >= 2+60*y and self.x <= 2+60*y+55 and self.y >= 35+20*x and self.y <= 35 + 20*x+15):

                        if ((self.y >= 35+20*x or self.y <= 35+20*x+15)
                                and (self.x >= 2+60*y and self.x <= 2+60*y+55)):
                            # Top or Bottom
                            self.delta_y = -self.delta_y
                            self.block[x][y] = 0
                            
                        elif ((self.x >= 2+60*y or self.x <= 2+60*y+55)
                              and (self.y >= 35+20*x and self.y <= 35+20*x+15)):
                            # Left or Right
                            self.delta_x = -self.delta_x
                            self.block[x][y] = 0

    def drawBotBlock(self):

        pygame.draw.rect(self.screen, (128, 128, 128), pygame.Rect(self.mouse_x-40, 450, 80, 10))

    def testBotCollision(self):

        # (mouse_x-40,450)      (mouse_x+40,450)
        #         +---------------------+

        if (self.y >= 448 and self.y <= 452):
            if (self.x >= self.mouse_x-40 and self.x <= self.mouse_x+40):
                self.delta_y = -self.delta_y

    def testEndCollision(self):

        if (self.y >= 499):
            self.reset()
            self.wait = True

    def render(self):

        self.screen.fill((0,0,0))
        
        self.drawBall()
        self.drawTopBlock()
        self.testTopCollision()
        self.drawBotBlock()
        self.testBotCollision()
        self.testEndCollision()
        
        pygame.display.flip()

    def renderStart(self):

        self.screen.fill((0,0,0))
                
        self.drawBotBlock()
        self.drawTopBlock()
              
        font = pygame.font.SysFont('Times New Roman', 48)
        label1 = font.render('WELCOME TO', 1, (255, 255, 255))
        label2 = font.render('CLICK TO START!', 1, (255, 255, 255))

        self.screen.blit(label1, (130, 200))
        self.screen.blit(label2, (100, 400))

        fontTitle = pygame.font.SysFont('Times New Roman',80)
        labelB = fontTitle.render('B', 1, (255, 69, 0))
        labelR = fontTitle.render('R', 1, (255, 255, 0))
        labelE = fontTitle.render('E', 1, (0, 255, 125))
        labelA = fontTitle.render('A', 1, (30, 0, 205))
        labelK = fontTitle.render('K', 1, (255, 69, 0))
        labelO = fontTitle.render('O', 1, (255, 255, 0))
        labelU = fontTitle.render('U', 1, (0, 255, 125))
        labelT = fontTitle.render('T', 1, (30, 0, 205))

        self.screen.blit(labelB, (100, 250))
        self.screen.blit(labelR, (150, 250))
        self.screen.blit(labelE, (200, 250))
        self.screen.blit(labelA, (250, 250))
        self.screen.blit(labelK, (300, 250))
        self.screen.blit(labelO, (350, 250))
        self.screen.blit(labelU, (400, 250))
        self.screen.blit(labelT, (450, 250))

    def renderRestart(self):

        self.screen.fill((0,0,0))
        self.drawBotBlock()
        self.drawTopBlock()
        font = pygame.font.SysFont('Times New Roman', 48)
        label = font.render('CLICK TO CONTINUE!', 1, (255, 255, 255))
        self.screen.blit(label, (55, 250))

    def renderFinish(self):
        
        font = pygame.font.SysFont('Times New Roman', 48)
        label = font.render('GAME FINISHED!', 1, (255, 255, 255))
        self.screen.blit(label, (105, 210))

    def mainloop(self):

        while True:
    
            for event in pygame.event.get():

                pressed = pygame.key.get_pressed()

                if (event.type == pygame.QUIT):
                        
                    pygame.quit()
                    sys.exit()

                elif (self.first_start and event.type == pygame.MOUSEBUTTONDOWN):
                    
                    self.first_start = False

                # Tracks the pad
                elif (event.type == pygame.MOUSEMOTION):
                    if (event.pos[0] < 40):
                        self.mouse_x = 40
                    elif (event.pos[0] > 560):
                        self.mouse_x = 560
                    else:
                        self.mouse_x = event.pos[0]

                # Resets the game
                elif (event.type == pygame.MOUSEBUTTONDOWN):

                    self.wait = False

            if (self.first_start):
                self.renderStart()
            elif (self.wait):
                self.renderRestart()
            elif (any (1 in sublist for sublist in self.block) and self.wait == False):
                self.render()
                pygame.time.wait(10)
            else:
                self.renderFinish()
                
            pygame.display.flip()

if __name__ == '__main__':
    BreakoutApp().mainloop()
