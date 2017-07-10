import pygame


class watertank:
    def __init__(self, sx, sy):
        pygame.init()
        self.sx = sx
        self.sy = sy
        self.screen = pygame.display.set_mode((self.sx, self.sy))
        self.container_x = 0.25*sx
        self.container_y = 0.25*sy
        self.container_w = 0.5*sx
        self.container_l = 0.75*sy
        self.water_x = 0.25*sx
        self.water_y = sy
        self.water_w = 0.5*sx
        self.water_l = -0.5*self.container_l
        self.container_rect = (self.container_x, self.container_y, self.container_w, self.container_l)
        self.water_rect = (self.water_x, self.water_y, self.water_w, self.water_l)
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (0, 0, 255), self.water_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), self.container_rect, 2)
        pygame.draw.rect(self.screen, (0, 0, 0), (self.container_x, self.container_y, self.container_w, 2))
        pygame.draw.rect(self.screen, (0, 0, 0), (self.container_x, self.container_y, self.container_w, -500))
        self.percentage = 100 * ((-1 * self.water_l) / self.container_l)
        pygame.display.flip()

    def fill_up(self):
        if self.num == 1:
            self.water_l -= 0.01 * self.container_l
        if self.num == 2:
            self.water_l -= 0.02 * self.container_l
        if self.num == 3:
            self.water_l -= 0.03 * self.container_l
        self.container_rect = (self.container_x, self.container_y, self.container_w, self.container_l)
        self.water_rect = (self.water_x, self.water_y, self.water_w, self.water_l)
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (0, 0, 255), self.water_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), self.container_rect, 2)
        pygame.draw.rect(self.screen, (0, 0, 0), (self.container_x, self.container_y, self.container_w, 2))
        pygame.draw.rect(self.screen, (0, 0, 0), (self.container_x, self.container_y, self.container_w, -500))
        self.percentage = 100 * ((-1 * self.water_l) / self.container_l)
        pygame.display.flip()

    def empty(self):
        if self.num == -1:
            self.water_l += 0.03 * self.container_l
        if self.num == -2:
            self.water_l += 0.02 * self.container_l
        if self.num == -3:
            self.water_l += 0.01 * self.container_l
        self.container_rect = (self.container_x, self.container_y, self.container_w, self.container_l)
        self.water_rect = (self.water_x, self.water_y, self.water_w, self.water_l)
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (0, 0, 255), self.water_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), self.container_rect, 2)
        pygame.draw.rect(self.screen, (0, 0, 0), (self.container_x, self.container_y, self.container_w, 2))
        pygame.draw.rect(self.screen, (0, 0, 0), (self.container_x, self.container_y, self.container_w, -500))
        self.percentage = 100 * ((-1 * self.water_l) / self.container_l)
        pygame.display.flip()

    def full(self):
        print("Empty")
        self.water_x = 0.25 * self.sx
        self.water_y = self.sy
        self.water_w = 0.5 * self.sx
        self.water_l = -0.5 * self.container_l
        pygame.draw.rect(self.screen, (0, 0, 255), self.water_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), self.container_rect, 2)
        pygame.draw.rect(self.screen, (0, 0, 0), (self.container_x, self.container_y, self.container_w, 2))
        pygame.draw.rect(self.screen, (0, 0, 0), (self.container_x, self.container_y, self.container_w, -500))
        self.percentage = 100 * ((-1 * self.water_l) / self.container_l)
        pygame.display.flip()

    def empty_2(self):
        print("Full")
        self.water_x = 0.25 * self.sx
        self.water_y = self.sy
        self.water_w = 0.5 * self.sx
        self.water_l = -0.5 * self.container_l
        pygame.draw.rect(self.screen, (0, 0, 255), self.water_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), self.container_rect, 2)
        pygame.draw.rect(self.screen, (0, 0, 0), (self.container_x, self.container_y, self.container_w, 2))
        pygame.draw.rect(self.screen, (0, 0, 0), (self.container_x, self.container_y, self.container_w, -500))
        self.percentage = 100 * ((-1 * self.water_l) / self.container_l)
        pygame.display.flip()

    def fill(self, num):
        self.num = num
        if num < 0 and self.water_l < 0:
            watertank.empty(self)

        elif num == 0 and self.water_l <= 0 and (-1 * self.water_l) < self.container_l:
            self.water_l += 0
            self.container_rect = (self.container_x, self.container_y, self.container_w, self.container_l)
            self.water_rect = (self.water_x, self.water_y, self.water_w, self.water_l)
            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, (0, 0, 255), self.water_rect)
            pygame.draw.rect(self.screen, (255, 255, 255), self.container_rect, 2)
            pygame.draw.rect(self.screen, (0, 0, 0), (self.container_x, self.container_y, self.container_w, 2))
            pygame.draw.rect(self.screen, (0, 0, 0), (self.container_x, self.container_y, self.container_w, -500))
            self.percentage = 100 * ((-1 * self.water_l) / self.container_l)
            pygame.display.flip()

        elif num > 0 and (-1 * self.water_l) < self.container_l:
            watertank.fill_up(self)

        if num <= 0 <= self.water_l:
            watertank.full(self)

        if num >= 0 and (-1 * self.water_l) >= self.container_l:
            watertank.empty_2(self)
