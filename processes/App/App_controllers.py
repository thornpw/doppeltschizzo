import random
import os

import pygame

import ablauf
import ablauf.apmn
from ablauf import pygamekern


# Classes
# ==========================================================================================
# The two worms of a player
# ******************************************************************************************
class WormDuo:
    # constants
    # --------------------------------------------------------------------------------------
    LEFT_WORM = 0
    RIGHT_WORM = 1

    # constructor
    # --------------------------------------------------------------------------------------
    def __init__(self, player_number):
        self.player_number = player_number
        self.fruits_collected = 0
        self.worms = [Worm(player_number, 0, DS.start_positions_left[player_number], 0), Worm(player_number, 1, DS.start_positions_right[player_number], 1)]
        self.game_over = False
        self.fruits = [Fruit(DS.worm_colors[player_number]), Fruit(DS.worm_colors[player_number + 1])]

    # create two new fruits. One for each worm
    # --------------------------------------------------------------------------------------
    def new_fruits(self):
        for _fruit in self.fruits:
            _top = random.randint(Grid.BLOCKS_MARGIN_TOP, Grid.BLOCKS_VERTICAL - 1)
            _left = random.randint(0, Grid.BLOCKS_HORIZONTAL - 1)
            _fruit.grid_position_top = _top
            _fruit.grid_position_left = _left
            _fruit.rect.top = _top * Grid.BLOCK_HEIGHT
            _fruit.rect.left = _left * Grid.BLOCK_WIDTH
            _fruit.visible = True

    # test collision
    # ---------------------------------------------------------------
    def test_collision(self):
        # test collision with other color fruit
        # -------------------------------------------------------
        if self.fruits[WormDuo.LEFT_WORM].visible:
            if self.worms[WormDuo.RIGHT_WORM].rect.colliderect(self.fruits[WormDuo.LEFT_WORM].rect):
                self.game_over = True

        if self.fruits[WormDuo.RIGHT_WORM].visible:
            if self.worms[WormDuo.LEFT_WORM].rect.colliderect(self.fruits[WormDuo.RIGHT_WORM].rect):
                self.game_over = True

        # test if a fruit was collected
        # -------------------------------------------------------
        for worm_number in range(0, 2):
            if self.fruits[worm_number].visible:
                if self.worms[worm_number].rect.colliderect(self.fruits[worm_number].rect):
                    _block = DS.empty_background.subsurface(self.fruits[worm_number].rect.left, self.fruits[worm_number].rect.top, DS.FRUIT_WIDTH, DS.FRUIT_HEIGHT)
                    ablauf.Automate.kernel.screen.blit(_block, (self.fruits[worm_number].rect.left, self.fruits[worm_number].rect.top))

                    ablauf.Automate.kernel.filled_rectangle(self.worms[worm_number].rect.left + 2, self.worms[worm_number].rect.top + 2, 12, 12, [127, 127, 127])
                    ablauf.Automate.kernel.filled_rectangle(self.worms[worm_number].rect.left + 4, self.worms[worm_number].rect.top + 4, 8, 8, DS.worm_colors[self.worms[worm_number].worm_number])

                    DS.grid.blocks[self.fruits[worm_number].grid_position_top][self.fruits[worm_number].grid_position_left] = 0
                    if self.fruits[worm_number].grid_position_top + 1 <= Grid.BLOCKS_VERTICAL-1:
                        DS.grid.blocks[self.fruits[worm_number].grid_position_top + 1][self.fruits[worm_number].grid_position_left] = 0
                    if self.fruits[worm_number].grid_position_left + 1 <= Grid.BLOCKS_HORIZONTAL-1:
                        DS.grid.blocks[self.fruits[worm_number].grid_position_top][self.fruits[worm_number].grid_position_left + 1] = 0
                    if self.fruits[worm_number].grid_position_top + 1 <= Grid.BLOCKS_VERTICAL-1 and self.fruits[worm_number].grid_position_left + 1 <= Grid.BLOCKS_HORIZONTAL-1:
                        DS.grid.blocks[self.fruits[worm_number].grid_position_top + 1][self.fruits[worm_number].grid_position_left + 1] = 0

                    DS.grid.blocks[(self.worms[worm_number].rect.top / Grid.BLOCK_HEIGHT)][(self.worms[worm_number].rect.left / Grid.BLOCK_WIDTH)] = worm_number

                    for loop in range(0, 30):
                        self.worms[WormDuo.LEFT_WORM].shorten_chain()
                        self.worms[WormDuo.RIGHT_WORM].shorten_chain()

                    if self.fruits_collected < 1:
                        self.fruits_collected += 1
                        self.fruits[worm_number].visible = False
                    else:
                        self.fruits_collected = 0
                        self.new_fruits()
                        DS.add_obstacle()

                    ablauf.Data.session["player_scores"][self.player_number] += self.worms[worm_number].collected_bonus
                    self.worms[worm_number].collected_bonus = 0


# One Worm
# ******************************************************************************************
class Worm(pygame.sprite.Sprite):
    def __init__(self, player_number, worm_number, initial_position, image_number):
        pygame.sprite.Sprite.__init__(self)
        # self.image = worm_images[image_number]
        # self.rect = self.image.get_rect()
        self.rect = pygame.Rect(0, 0, 16, 16)
        self.rect.topleft = initial_position
        self.direction = 3
        self.player_number = player_number
        self.chain = []
        self.sync_movement_rendering = 0
        self.speed = DS.SPEED_NORMAL
        self.worm_number = worm_number
        self.moved = 0
        self.delay = 0
        self.chain_remove_delay = 2
        self.bonus = 1  # actual bonus
        self.collected_bonus = 0  # already collected bonus. Bonus gained when a fruit is collected
        self.lives = 3

    def render(self):
        _test = DS.grid.blocks[(self.rect.top / Grid.BLOCK_HEIGHT)][(self.rect.left / Grid.BLOCK_WIDTH)]
        if _test != 0:
            DS.worm_duos[self.player_number].game_over = True
            print("Game Over")
        else:
            DS.grid.blocks[(self.rect.top / Grid.BLOCK_HEIGHT)][(self.rect.left / Grid.BLOCK_WIDTH)] = self.player_number + 1
            self.chain.append([self.rect.left, self.rect.top])
            # pygamekern.Kernel.screen.blit(self.image, self.rect)
            ablauf.Automate.kernel.filled_rectangle(self.rect.left + 2, self.rect.top + 2, 12, 12, [127, 127, 127])
            ablauf.Automate.kernel.filled_rectangle(self.rect.left + 4, self.rect.top + 4, 8, 8, DS.worm_colors[self.worm_number])
            self.sync_movement_rendering = 1

            if self.chain_remove_delay == 0:
                self.shorten_chain()
                self.chain_remove_delay = 2
            else:
                self.chain_remove_delay -= 1

    def update(self):
        if self.delay == 0:
            if self.direction == DS.LEFT:
                if self.rect.left > DS.MARGIN_LEFT:
                    self.rect.left -= Grid.BLOCK_WIDTH
                else:
                    self.rect.left = DS.MARGIN_RIGHT

            if self.direction == DS.TOP:
                if self.rect.top > DS.MARGIN_TOP:
                    self.rect.top -= Grid.BLOCK_HEIGHT
                else:
                    self.rect.top = DS.MARGIN_BOTTOM
            if self.direction == DS.RIGHT:
                if self.rect.left < DS.MARGIN_RIGHT:
                    self.rect.left += Grid.BLOCK_WIDTH
                else:
                    self.rect.left = DS.MARGIN_LEFT

            if self.direction == DS.DOWN:
                if self.rect.top < DS.MARGIN_BOTTOM:
                    self.rect.top += Grid.BLOCK_HEIGHT
                else:
                    self.rect.top = DS.MARGIN_TOP

            self.render()
            self.delay = self.speed
            self.collected_bonus += self.bonus
        else:
            self.delay -= 1

    def shorten_chain(self):
        if (self.chain.__len__()) > 0:
            _block = DS.empty_background.subsurface((self.chain[0][0], self.chain[0][1], Grid.BLOCK_WIDTH, Grid.BLOCK_HEIGHT))
            ablauf.Automate.kernel.screen.blit(_block, (self.chain[0][0], self.chain[0][1]))
            DS.grid.blocks[self.chain[0][1] / Grid.BLOCK_WIDTH][self.chain[0][0] / Grid.BLOCK_HEIGHT] = 0
            del (self.chain[0])

    def clear_chain(self):
        if self.chain.__len__() > 0:
            _top = self.chain[0][1]
            _left = self.chain[0][0]
            while (self.chain.__len__()) >= 1:
                _length = self.chain.__len__() - 1
                _block = DS.empty_background.subsurface((self.chain[_length][0], self.chain[_length][1], Grid.BLOCK_WIDTH, Grid.BLOCK_HEIGHT))
                ablauf.Automate.kernel.screen.blit(_block, (self.chain[_length][0], self.chain[_length][1]))
                DS.grid.blocks[self.chain[_length][1] / Grid.BLOCK_WIDTH][self.chain[_length][0] / Grid.BLOCK_HEIGHT] = 0
                del (self.chain[_length])

            self.rect.top = _top
            self.rect.left = _left


class Fruit(pygame.sprite.Sprite):
    # constructor
    # --------------------------------------------------------------------------------------
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([DS.FRUIT_WIDTH, DS.FRUIT_HEIGHT])
        self.color = color
        self.rect = self.image.get_rect()
        self.visible = True
        self.grid_position_top = 0
        self.grid_position_left = 0

    def update(self):
        pass

    def render(self):
        # pygamekern.Kernel.screen.blit(self.image, self.rect)
        ablauf.Automate.kernel.filled_rectangle(self.rect.left + 2, self.rect.top + 2, 12, 12, [0, 0, 0])
        ablauf.Automate.kernel.filled_rectangle(self.rect.left + 4, self.rect.top + 4, 8, 8, self.color)


class Wall(pygame.sprite.Sprite):
    # constructor
    # --------------------------------------------------------------------------------------
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0, 16 * Grid.BLOCKS_MARGIN_TOP, 16, 16 * (Grid.BLOCKS_VERTICAL-Grid.BLOCKS_MARGIN_TOP))
        self.visible = True

    def update(self):
        self.rect.left += 1

    def render(self):
        # pygamekern.Kernel.screen.blit(self.image, self.rect)
        if self.rect.left > 0:
            print(self.rect.left-16)
            ablauf.Automate.kernel.screen.blit(DS.empty_background, (self.rect.left-16, self.rect.top, 16, 16 * (Grid.BLOCKS_VERTICAL-Grid.BLOCKS_MARGIN_TOP)))
        if self.rect.left < (Grid.BLOCKS_HORIZONTAL-2) * 16:
            #ablauf.Automate.kernel.filled_rectangle(self.rect.left, self.rect.top, 16, 16 * Grid.BLOCKS_VERTICAL, [0, 0, 0])
            pass
        else:
            self.rect.left = 0


class Grid():
    # constants
    # --------------------------------------------------------------------------------------
    BLOCK_WIDTH = 16
    BLOCK_HEIGHT = 16
    BLOCKS_VERTICAL = 50
    BLOCKS_HORIZONTAL = 64
    BLOCKS_MARGIN_TOP = 3

    # constructor
    # --------------------------------------------------------------------------------------
    def __init__(self):
        self.blocks= []

     # reset
     # ----------------------------------------------------------------------------------
    def reset(self):
        self.blocks = []

        for row in range(0, Grid.BLOCKS_VERTICAL):
            self.blocks.append([])
            for column in range(0, Grid.BLOCKS_HORIZONTAL):
                self.blocks[row].append(0)

# The game class
# ******************************************************************************************
class DS:
    # constants
    # --------------------------------------------------------------------------------------
    # Directions
    # --------------------------------------------------------------------------------------
    STOPPED = 0
    LEFT = 1
    TOP = 2
    RIGHT = 3
    DOWN = 4

    # Speed
    # --------------------------------------------------------------------------------------
    SPEED_SLOW = 50
    SPEED_NORMAL = 30
    SPEED_FAST = 4

    # Screen margins
    # --------------------------------------------------------------------------------------
    MARGIN_LEFT = 0
    MARGIN_RIGHT = 1008
    MARGIN_TOP = 48
    MARGIN_BOTTOM = 784

    FRUIT_WIDTH = 16
    FRUIT_HEIGHT = 16

    WALL_WIDTH = 16
    WALL_HEIGHT = 16

    # Lists
    # --------------------------------------------------------------------------------------
    worm_colors = [(205, 205, 0), (105, 105, 0), (255, 80, 0), (255, 120, 0), (255, 160, 0), (255, 200, 0), (255, 240, 0), (255, 255, 0)]
    start_positions_left = [[160, 160], [0, 40], [0, 80], [0, 120], [0, 160], [0, 200], [0, 240], [0, 280]]
    start_positions_right = [[320, 320], [400, 40], [400, 80], [400, 120], [400, 160], [400, 200], [400, 240], [400, 280]]

    # Dynamic variables
    # --------------------------------------------------------------------------------------
    fruit_duos_collected = 0
    level = 0
    worm_duos = []
    grid = Grid()
    wall = Wall()

    # surfaces
    # --------------------------------------------------------------------------------------
    empty_background = pygame.Surface([ablauf.Data.configuration["width"], ablauf.Data.configuration["height"]])
    obstacle = pygame.image.load(os.path.join("media", "images", "wall2.png"))

    # images
    # --------------------------------------------------------------
    # green = pygame.image.load(os.path.join("media", "images", "Grass16.png"))

    # worm_images = [
    #    pygame.image.load(os.path.join("media", "images", "rot8x8.png")),
    #    pygame.image.load(os.path.join("media", "images", "gelb8x8.png"))
    # ]

    # initial drawing of the background. Also save the background to redraw ereased stuff
    # -------------------------------------------------------------------------------------
    @staticmethod
    def initialize_playground():
        for bg_row in range(0, Grid.BLOCKS_VERTICAL):
            for bg_column in range(0, Grid.BLOCKS_HORIZONTAL):
                ablauf.Automate.kernel.filled_rectangle(bg_column * 16, 0 + bg_row * 16, 16, 16, [235, 235, 235])
                ablauf.Automate.kernel.filled_rectangle(bg_column * 16, 0 + bg_row * 16, 15, 15, [255, 255, 255])
                DS.empty_background.blit(ablauf.Automate.kernel.screen, (DS.MARGIN_LEFT + bg_column * 32, 0 + bg_row * 32, 32, 32))

    # render
    # --------------------------------------------------------------------------------------
    @staticmethod
    def render():
        # status
        # ----------------------------------------------------------------------------------
        ablauf.Automate.kernel.filled_rectangle(0, 0, 1024, 16, [0, 0, 200])
        ablauf.Automate.kernel.filled_rectangle(0, 16, 1024, 32, [0, 0, 255])
        ablauf.Automate.kernel.scalable_text("SCORE:{0}".format(ablauf.Data.session["player_scores"][0]), 20, 20, None, 20, (255, 255, 255))

        _left_lives = DS.worm_duos[0].worms[0].lives
        _left_stars = ""
        for _i in range(0, _left_lives):
            _left_stars += "*"

        _right_lives = DS.worm_duos[0].worms[1].lives
        _right_stars = ""
        for _i in range(0, _right_lives):
            _right_stars += "*"

        ablauf.Automate.kernel.scalable_text(_left_stars, 100, 20, None, 20, (255, 255, 255))
        ablauf.Automate.kernel.scalable_text(_right_stars, 140, 20, None, 20, (255, 255, 255))

        ablauf.Automate.kernel.scalable_text("8 8 8 8", 200, 20, None, 20, (255, 255, 255))

        # players
        # ----------------------------------------------------------------------------------
        for _player in DS.worm_duos:
            for _worm in _player.worms:
                _worm.update()

        # fruits
        # ----------------------------------------------------------------------------------
        for _player in DS.worm_duos:
            for fruit in _player.fruits:
                if fruit.visible:
                    fruit.render()

        # wall
        # ----------------------------------------------------------------------------------
        if DS.wall.visible:
            DS.wall.render()
            DS.wall.update()

    # test if game is over
    # --------------------------------------------------------------------------------------
    @staticmethod
    def test_game_over():
        _continue = False

        for player in range(0, ablauf.Data.session["parameters"]["number_of_players"]):
            if DS.worm_duos[player].game_over is False:
                _continue = True

        return _continue

    # create a new obstacle
    # --------------------------------------------------------------------------------------
    @staticmethod
    def add_obstacle():
        _found = False
        _counter = 0

        while not _found:
            _top = random.randint(Grid.BLOCKS_MARGIN_TOP, Grid.BLOCKS_VERTICAL - 1)
            _left = random.randint(0, Grid.BLOCKS_HORIZONTAL - 1)
            _counter += 1

            if DS.grid.blocks[_top][_left] == 0:
                ablauf.Automate.kernel.screen.blit(DS.obstacle, (_left * DS.WALL_WIDTH, _top * DS.WALL_HEIGHT))
                DS.grid.blocks[_top][_left] = 99
                _found = True

            if _counter == 10:
                _found = True

    # reset the game variables
    # --------------------------------------------------------------------------------------
    @staticmethod
    def reset():
        # reset game
        # ----------------------------------------------------------------------------------
        DS.fruit_duos_collected = 0
        DS.level = 0

        # reset players
        # ----------------------------------------------------------------------------------
        DS.worm_duos = []

        for player in range(0, ablauf.Data.session["parameters"]["number_of_players"]):
            _wormduo = WormDuo(player)
            DS.worm_duos.append(_wormduo)
            _wormduo.new_fruits()

        # reset grid
        # ----------------------------------------------------------------------------------
        DS.grid.reset()



# controlling
# ====================================================================================================================
# speed
# ********************************************************************************************************************
def left_worm_speedup(controller):
    DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].speed = DS.SPEED_FAST
    DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].bonus = 10


def left_worm_normal_speed(controller):
    DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].speed = DS.SPEED_NORMAL
    DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].bonus = 1


def left_worm_slowdown(controller):
    DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].speed = DS.SPEED_SLOW
    DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].bonus = 0


def right_worm_speedup(controller):
    DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].speed = DS.SPEED_FAST
    DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].bonus = 10


def right_worm_normal_speed(controller):
    DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].speed = DS.SPEED_NORMAL
    DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].bonus = 1


def right_worm_slowdown(controller):
    DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].speed = DS.SPEED_SLOW
    DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].bonus = 0


# directions
# ********************************************************************************************************************
def left_top_pressed(controller):
    if DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].sync_movement_rendering:
        if DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].direction in [DS.LEFT, DS.RIGHT]:
            DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].direction = DS.TOP
            DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].sync_movement_rendering = False


def left_down_pressed(controller):
    if DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].sync_movement_rendering:
        if DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].direction in [DS.LEFT, DS.RIGHT]:
            DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].direction = DS.DOWN
            DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].sync_movement_rendering = False


def left_left_pressed(controller):
    if DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].sync_movement_rendering:
        if DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].direction in [DS.TOP, DS.DOWN]:
            DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].direction = DS.LEFT
            DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].sync_movement_rendering = False


def left_right_pressed(controller):
    if DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].sync_movement_rendering:
        if DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].direction in [DS.TOP, DS.DOWN]:
            DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].direction = DS.RIGHT
            DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].sync_movement_rendering = False


def right_top_pressed(controller):
    if DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].sync_movement_rendering:
        if DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].direction in [DS.LEFT, DS.RIGHT]:
            DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].direction = DS.TOP
            DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].sync_movement_rendering = False


def right_down_pressed(controller):
    if DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].sync_movement_rendering:
        if DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].direction in [DS.LEFT, DS.RIGHT]:
            DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].direction = DS.DOWN
            DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].sync_movement_rendering = False


def right_left_pressed(controller):
    if DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].sync_movement_rendering:
        if DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].direction in [DS.TOP, DS.DOWN]:
            DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].direction = DS.LEFT
            DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].sync_movement_rendering = False


def right_right_pressed(controller):
    if DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].sync_movement_rendering:
        if DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].direction in [DS.TOP, DS.DOWN]:
            DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].direction = DS.RIGHT
            DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].sync_movement_rendering = False


# analog buttons
# ********************************************************************************************************************
def button_l3_pressed(controller):
    print("hallo")
    if DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].lives > 0:
        DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].clear_chain()
        DS.worm_duos[controller.number].worms[WormDuo.LEFT_WORM].lives -= 1
    else:
        DS.worm_duos[controller.number].game_over = True


def button_r3_pressed(controller):
    if DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].lives > 0:
        DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].clear_chain()
        DS.worm_duos[controller.number].worms[WormDuo.RIGHT_WORM].lives -= 1
    else:
        DS.worm_duos[controller.number].game_over = True


# extras
# ********************************************************************************************************************
def button_topleft_pressed(controller):
    print("topleft")


def button_topright_pressed(controller):
    print("topright")


def button_downleft_pressed(controller):
    print("downleft")


def button_downright_pressed(controller):
    print("downright")


# State classes
# ===================================================================================================================
# init task
# *******************************************************************************************************************
class Init(ablauf.apmn.Task):
    def __init__(self, config):
        ablauf.apmn.Task.__init__(self, config)

    def task(self):
        # initialize pygame
        # -------------------------------------------------------------------
        ablauf.Automate.kernel.screen = pygame.display.set_mode([ablauf.Data.configuration["width"], ablauf.Data.configuration["height"]])

        # initialize game
        # --------------------------------------------------------------------
        DS.reset()


# <ab> start id:Stema
# Stema task
# ****************************************************************************
class Stema(ablauf.apmn.SubProcess):
    def __init__(self, config):
        ablauf.apmn.SubProcess.__init__(self, config)

    def task(self):
        pass


# <ab> end id: Stema

# <ab> start id:menu
# menu task
# ****************************************************************************
class menu(ablauf.apmn.UserTask):
    def __init__(self, config):
        ablauf.apmn.UserTask.__init__(self, config)

    def task(self):
        pass


# <ab> end id: menu

# <ab> start id:options
# options task
# ****************************************************************************
class options(ablauf.apmn.UserTask):
    def __init__(self, config):
        ablauf.apmn.UserTask.__init__(self, config)

    def task(self):
        pass


# <ab> end id: options

# <ab> start id:credits
# credits task
# ****************************************************************************
class credits(ablauf.apmn.UserTask):
    def __init__(self, config):
        ablauf.apmn.UserTask.__init__(self, config)

    def task(self):
        pass


# <ab> end id: credits

# <ab> start id:players
# players task
# ****************************************************************************
class players(ablauf.apmn.UserTask):
    def __init__(self, config):
        ablauf.apmn.UserTask.__init__(self, config)

    def task(self):
        pass


# <ab> end id: players

# <ab> start id:playername
# playername task
# ****************************************************************************
class playername(ablauf.apmn.UserTask):
    def __init__(self, config):
        ablauf.apmn.UserTask.__init__(self, config)

    def task(self):
        pass


# <ab> end id: playername

# <ab> start id:highscore
# highscore task
# ****************************************************************************
class highscore(ablauf.apmn.UserTask):
    def __init__(self, config):
        ablauf.apmn.UserTask.__init__(self, config)

    def task(self):
        pass


# <ab> end id: highscore


# <ab> start id:game_init
# game_init task
# ****************************************************************************
class game_init(ablauf.apmn.Task):
    def __init__(self, config):
        ablauf.apmn.Task.__init__(self, config)

    def task(self):
        # Set action callback functions
        ablauf.Automate.input_handler.Action('DPAD_TOP', 1, 'DPad top', 'Top', 0, 0, 0, 0, )
        ablauf.Automate.input_handler.Action('DPAD_DOWN', 2, 'DPad down', 'Down', 0, 0, 0, 0)
        ablauf.Automate.input_handler.Action('DPAD_LEFT', 4, 'DPad left', 'Left', 0, 0, 0, 0)
        ablauf.Automate.input_handler.Action('DPAD_RIGHT', 8, 'DPad right', 'Right', 0, 0, 0, 0)
        ablauf.Automate.input_handler.Action('BUTTON_TOP', 4096, 'Button top', 'BTop', 0, 0, 0, 0)
        ablauf.Automate.input_handler.Action('BUTTON_DOWN', 8192, 'Button down', 'BDown', 0, 0, 0, 0)
        ablauf.Automate.input_handler.Action('BUTTON_LEFT', 16384, 'Button left', 'BLeft', 0, 0, 0, 0)
        ablauf.Automate.input_handler.Action('BUTTON_RIGHT', 32768, 'Button right', 'BRight', 0, 0, 0, 0)
        ablauf.Automate.input_handler.Action('SHOULDER_L1', 65536, 'Shoulder L1', 'L1', 0, 0, 0, 0, left_worm_speedup, left_worm_normal_speed)
        ablauf.Automate.input_handler.Action('SHOULDER_L2', 131072, 'Shoulder L2', 'L2', 0, 0, 0, 0, left_worm_slowdown, left_worm_normal_speed)
        ablauf.Automate.input_handler.Action('SHOULDER_R1', 262144, 'Shoulder R1', 'R1', 0, 0, 0, 0, right_worm_speedup, right_worm_normal_speed)
        ablauf.Automate.input_handler.Action('SHOULDER_R2', 524288, 'Shoulder R2', 'R2', 0, 0, 0, 0, right_worm_slowdown, right_worm_normal_speed)
        ablauf.Automate.input_handler.Action('ANALOG_L3', 1048576, 'Analog L3', 'L3', 0, 0, 0, 0, button_l3_pressed)
        ablauf.Automate.input_handler.Action('ANALOG_R3', 2097152, 'Analog R3', 'R3', 0, 0, 0, 0, button_r3_pressed)
        ablauf.Automate.input_handler.Action('BUTTON_START', 4194304, 'Button start', 'BStart', 0, 0, 0, 0)
        ablauf.Automate.input_handler.Action('BUTTON_SELECT', 8388608, 'Button select', 'BSelect', 0, 0, 0, 0)
        ablauf.Automate.input_handler.Action('LEFT_TOP', 16777216, 'Left analog stick top', 'LT', 0, 0, 0, 0, left_top_pressed)
        ablauf.Automate.input_handler.Action('LEFT_DOWN', 33554432, 'Left analog stick down', 'LD', 0, 0, 0, 0, left_down_pressed)
        ablauf.Automate.input_handler.Action('LEFT_LEFT', 67108864, 'Left analog stick left', 'LL', 0, 0, 0, 0, left_left_pressed)
        ablauf.Automate.input_handler.Action('LEFT_RIGHT', 134217728, 'Left analog stick right', 'LR', 0, 0, 0, 0, left_right_pressed)
        ablauf.Automate.input_handler.Action('RIGHT_TOP', 268435456, 'Right analog stick top', 'RT', 0, 0, 0, 0, right_top_pressed)
        ablauf.Automate.input_handler.Action('RIGHT_DOWN', 536870912, 'Right analog stick down', 'RD', 0, 0, 0, 0, right_down_pressed)
        ablauf.Automate.input_handler.Action('RIGHT_LEFT', 1073741824, 'Right analog stick left', 'RL', 0, 0, 0, 0, right_left_pressed)
        ablauf.Automate.input_handler.Action('RIGHT_RIGHT', 2147483648, 'Right analog stick right', 'RR', 0, 0, 0, 0, right_right_pressed)

        # Set direction callback functions
        ablauf.Automate.input_handler.Direction('DPAD_TOP', 0b0001, 'DPad top', 'Top')
        ablauf.Automate.input_handler.Direction('DPAD_DOWN', 0b0010, 'DPad down', 'Down')
        ablauf.Automate.input_handler.Direction('DPAD_LEFT', 0b0100, 'DPad left', 'Left')
        ablauf.Automate.input_handler.Direction('DPAD_RIGHT', 0b1000, 'DPad right', 'Right')
        ablauf.Automate.input_handler.Direction('DPAD_TOPLEFT', 0b0101, 'DPad top left', 'Top Left', button_topleft_pressed)
        ablauf.Automate.input_handler.Direction('DPAD_TOPRIGHT', 0b1001, 'DPad top right', 'Top Right', button_topright_pressed)
        ablauf.Automate.input_handler.Direction('DPAD_DOWNLEFT', 0b0110, 'DPad down left', 'Down Left', button_downleft_pressed)
        ablauf.Automate.input_handler.Direction('DPAD_DOWNRIGHT', 0b1010, 'DPad down right', 'Down Right', button_downright_pressed)

        # ablauf.Automate.input_handler.controllers[0].bits -= 4096

        # reset game
        # -------------------------------------------------------------------
        DS.reset()

        # reset scores
        # -------------------------------------------------------------------
        for player in range(0, ablauf.Data.session["parameters"]["number_of_players"]):
            ablauf.Data.session["player_scores"][player] = 0

# <ab> end id: game_init

# <ab> start id:game
# game task
# ****************************************************************************
class game(ablauf.apmn.Game):
    def __init__(self, config):
        ablauf.apmn.Game.__init__(self, config)

    def task(self):
        is_running = True

        # initial drawing
        # --------------------------------------------------------------
        DS.initialize_playground()

        # main loop
        # --------------------------------------------------------------
        while is_running:
            # sync
            # ----------------------------------------------------------
            ablauf.Automate.kernel.clock_sync(200)

            # loop over events
            # ----------------------------------------------------------
            for event in pygame.event.get():
                # test if program should quit
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        is_running = False
                else:
                    # map event to actions
                    # ==================================================
                    ablauf.Automate.input_handler.call_event_and_direction(event)

            # test collision
            # ----------------------------------------------------------
            for worm_duo in DS.worm_duos:
                worm_duo.test_collision()

            # render
            # ----------------------------------------------------------
            DS.render()

            # flip screens
            # ----------------------------------------------------------
            pygame.display.update()

            # test if the game is over
            # ----------------------------------------------------------
            if is_running:
                is_running = DS.test_game_over()

# <ab> end id: game
