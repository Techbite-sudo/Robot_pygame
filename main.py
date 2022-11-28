import pygame
from pygame import mixer

# General setup
pygame.init()
clock = pygame.time.Clock()

# button class


class Button():
    def __init__(self, x, y, image, scale):
        self.image = pygame.transform.scale(
            image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action


def zoom(path, sizeX):
    return pygame.transform.smoothscale(pygame.image.load(path), (sizeX / 2, 130))

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sequence_animation = False
        self.sprites = []

        self.sprites.append(zoom("images/Subject 6.png", 150))
        self.sprites.append(zoom("images/Subject 7.png", 150))
        self.sprites.append(zoom("images/Subject 8.png", 173))
        self.sprites.append(zoom("images/Subject 9.png", 189))
        self.sprites.append(zoom("images/Subject 10.png", 203))
        self.sprites.append(zoom("images/Subject 11.png", 192))
        self.sprites.append(zoom("images/Subject 12.png", 164))
        self.sprites.append(zoom("images/Subject 12.png", 164))
        self.sprites.append(zoom("images/Subject 14.png", 164))
        self.sprites.append(zoom("images/Subject 14.png", 164))
        self.sprites.append(zoom("images/Subject 14.png", 164))
        self.sprites.append(zoom("images/Subject 12.png", 164))
        self.sprites.append(zoom("images/Subject 12.png", 164))
        self.sprites.append(zoom("images/Subject 16.png", 164))
        self.sprites.append(zoom("images/Subject 16.png", 164))
        self.sprites.append(zoom("images/Subject 16.png", 164))
        self.sprites.append(zoom("images/Subject 12.png", 164))
        self.sprites.append(zoom("images/Subject 12.png", 164))
        self.sprites.append(zoom("images/Subject 11.png", 192))
        self.sprites.append(zoom("images/Subject 10.png", 203))
        self.sprites.append(zoom("images/Subject 9.png", 189))
        self.sprites.append(zoom("images/Subject 8.png", 173))
        self.sprites.append(zoom("images/Subject 7.png", 150))
        self.sprites.append(zoom("images/Subject 6.png", 150))
        self.sprites.append(zoom("images/Subject 17.png", 150))
        self.sprites.append(zoom("images/Subject 17.png", 150))
        self.sprites.append(zoom("images/Subject 18.png", 150))
        self.sprites.append(zoom("images/Subject 18.png", 150))
        self.sprites.append(zoom("images/Subject 19.png", 150))
        self.sprites.append(zoom("images/Subject 19.png", 150))
        self.sprites.append(zoom("images/Subject 18.png", 150))
        self.sprites.append(zoom("images/Subject 18.png", 150))
        self.sprites.append(zoom("images/Subject 17.png", 150))
        self.sprites.append(zoom("images/Subject 17.png", 150))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.sequence_animation = True

    def update(self, speed):
        if self.sequence_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.sequence_animation = False
                # button1.change_text("Animate", bg="navy")

        self.image = self.sprites[int(self.current_sprite)]


# Game Screen
screen_width = 848
screen_height = 477
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animate")

# load button images and background image
animate_img = pygame.image.load('images/animate.png').convert_alpha()
bg = pygame.image.load("images/bg.webp").convert_alpha()

# create button instances, player instances and groups
player = Player(300, 250)
animate_button = Button(350, 5, animate_img, 0.5)

moving_sprites = pygame.sprite.Group()
moving_sprites.add(player)
fps = 0.15
# Background sound
mixer.music.load('audio/Robot-Songs-Robot-says.wav')
mixer.music.set_volume(0.1)
mixer.music.play(-1)

# game loop
run = True
while run:
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            player.animate()
    # Drawing
    screen.fill([255, 255, 255])
    screen.blit(pygame.transform.smoothscale(bg, (848, 477)), (0, 0))
    moving_sprites.draw(screen)

    if animate_button.draw(screen):
        player.animate()
        
    pygame.display.update()
    moving_sprites.update(fps)

    pygame.display.flip()
    clock.tick(60)
