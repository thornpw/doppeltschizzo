import pygame

import steuer

# player object
# --------------------------------------------------------------
class Worm(pygame.sprite.Sprite):
    def __init__(self, initial_position, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([7, 7])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position

    def render(self):
        screen.blit(self.image, self.rect)


# initialize variables
# --------------------------------------------------------------
worm_colors = [(255, 0, 0), (255, 40, 0), (255, 80, 0), (255, 120, 0), (255, 160, 0), (255, 200, 0), (255, 240, 0), (255, 255, 0)]
start_positions = [[0, 0], [40, 40], [80, 80], [120, 120], [160, 160], [200, 200], [240, 240], [280, 280]]
worms = []
is_running = True
number_of_players = 8

for player in range(0, number_of_players):
    worms.append(Worm(start_positions[player], worm_colors[player]))

# initialize pygame
# --------------------------------------------------------------
screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()

# main loop
# --------------------------------------------------------------
while is_running:
    clock.tick(60)

    # loop over events
    for event in pygame.event.get():
        # test if program should quit
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                worms[0].rect.top -= 3
            if pressed[pygame.K_DOWN]:
                worms[0].rect.top += 3
            if pressed[pygame.K_LEFT]:
                worms[0].rect.left -= 3
            if pressed[pygame.K_RIGHT]:
                worms[0].rect.left += 3
        else:
            # map event to actions
            #  ==================================================
            steuer.get_action(event)

    # test if steuer direction is set
    # ===========================================================
    for controller_number in range(0, pygame.joystick.get_count()):
        if steuer.controllers[controller_number].bits & steuer.DPAD_TOP:
            worms[controller_number].rect.top -= 3
        if steuer.controllers[controller_number].bits & steuer.DPAD_DOWN:
            worms[controller_number].rect.top += 3
        if steuer.controllers[controller_number].bits & steuer.DPAD_LEFT:
            worms[controller_number].rect.left -= 3
        if steuer.controllers[controller_number].bits & steuer.DPAD_RIGHT:
            worms[controller_number].rect.left += 3

    # render
    # ----------------------------------------------------------
    screen.fill([0, 0, 0])  # blank the screen.

    for worm in worms:
        worm.render()

    pygame.display.update()
