import arcade
import os

# Constants for width and height of window
screenWidth, screenHeight = 1000, 550

# Sprite scale constants
dojaScaling = 0.45
tileScaling = 0.5

# Constants for the physics of the game
moveSpeed, gravity, jumpSpeed = 7, 4.5, 200

# Margin constants between Doja and the screen edges
topMargin, bottomMargin, rightMargin, leftMargin = 200, 100, 200, 100

# Constants as 'state' of the game, eg. Menu, Game and the Game Over
gameMenu, gameRunning, gameOver = 0, 1, 2

# Constants to track if Doja is facing left or right
# rightFacing, leftFacing = 0, 1
# updatePerFrame = 5
# def getSpritePair(fname):
    # """Returns a list of a sprite and its mirror image"""
    # return [arcade.load_texture(fname, scale = dojaScaling), arcade.load_texture(fname, scale= dojaScaling, mirrored = True)]

# class Doja(arcade.Sprite):
    # def __init__(self):
        # Set up parent class
        # super().__init__()

        # Sets character to face right by default
        # self.dojaFaceDirection = rightFacing

        # Animates image into a sequence
        # self.cur_texture = 0
        # Tracks state
        # self.jump = False

        # Load Doja's idle, jump and fall animation
        # self.idlePair = getSpritePair("sprites/Doja/doja_idle.png")
        # self.jumpPair = getSpritePair("sprites/Doja/doja_jumping.png")
        # self.fallPair = getSpritePair("sprites/Doja/doja_landing.png")

        # Load Doja's walking animation
        # self.walkTexture = []
        # for i in range(4):
            # texture = getSpritePair(f"sprites/Doja/doja_walking_{i}.png")
            # self.walkTexture.append(texture)

    # def update_animation(self, delta_time: float = 1/60):
        # Changes Doja's facing direction if needed
        # if self.change_x < 0 and self.dojaFaceDirection == rightFacing:
            # self.dojaFaceDirection = leftFacing
        # elif self.change_x > 0 and self.dojaFaceDirection == leftFacing:
            # self.dojaFaceDirection = rightFacing

        # Idle animation
        # if self.change_x == 0:
            # self.texture = self.idlePair[self.dojaFaceDirection]
            # return

        # Walking animation
        # self.cur_texture += 1
        # if self.cur_texture > 4 * updatePerFrame:
            # self.cur_texture = 0
        # self.texture = self.walkTexture[self.cur_texture // updatePerFrame][self.dojaFaceDirection]

        # Jumping animation
        # if self.jump:
            # if self.change_y > 0:
                # self.texture = self.jumpPair[self.dojaFaceDirection]
            # else:
                # self.texture = self.jumpPair[self.dojaFaceDirection]

class Feline(arcade.Window):
    """Main Game"""

    def __init__(self, screenWidth, screenHeight, title):

        # Call the parent class's init function
        super().__init__(screenWidth, screenHeight, title)

        # Set path for program
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Set physics for the game
        self.physicsDoja = None

        # Sprite lists
        self.miceList, self.dojaList, self.milkList, self.sandList, self.cactusList = None, None, None, None, None

        # Disappears the mouse when it is over the window
        self.set_mouse_visible(False)

        # Sets up the sprites
        self.dojaSprite, self.miceSprite = None, None

        # Tracks which key is pressed
        self.pressUp, self.pressDown, self.pressRight, self.pressLeft = False, False, False, False

        # Tracks scrolling
        self.bottomView, self.leftView = 0, 0
        self.mapEnd = 0

        # Tracks score
        self.score = 0
        self.scoreSprite = None

        # Tracks health
        self.health = 3
        self.healthSprite = None

        # Load sounds
        self.miceEatenSound = arcade.load_sound("soundfx/mice.wav")
        self.backgroundMusic = arcade.load_sound("soundfx/rules.wav")
        self.cactusSound = arcade.load_sound("soundfx/cactus.wav")
        self.milkSound = arcade.load_sound("soundfx/milk.wav")
        self.jumpSound = arcade.load_sound("soundfx/jump/wav")

        # Puts state of the game as gameMenu
        self.currentState = gameMenu

        # Sets textures for text
        self.gameOverText, self.startText, self.restartText = None, None, None

    def setup(self):
        """Sets up the game, function is used for restarting the game."""
        # Plays background music
        # if self.currentState == gameRunning:
        arcade.play_sound(self.backgroundMusic)

        # Sets sprite lists
        self.dojaList = arcade.SpriteList()

        # Sets up the player
        # self.dojaSprite = arcade.AnimatedWalkingSprite()
        self.dojaSprite = arcade.Sprite("sprites/Doja/doja_idle.png", dojaScaling)
        self.dojaSprite.center_x, self.dojaSprite.center_y = 100, 100
        self.dojaList.append(self.dojaSprite)

        # Load textures/animations for Doja's idle, jump and walk
        # self.dojaSprite.stand_right_textures = []
        # self.dojaSprite.stand_right_textures.append(arcade.load_texture("sprites/Doja/doja_idle.png"))
        # self.dojaSprite.stand_left_textures = []
        # self.dojaSprite.stand_left_textures.append(arcade.load_texture("sprites/Doja/doja_idle.png", mirrored=True))

        # self.dojaSprite.walk_right_textures = []
        # self.dojaSprite.walk_right_textures.append(arcade.load_texture("sprites/Doja/doja_walking_0.png"))
        # self.dojaSprite.walk_right_textures.append(arcade.load_texture("sprites/Doja/doja_walking_1.png"))
        # self.dojaSprite.walk_right_textures.append(arcade.load_texture("sprites/Doja/doja_walking_2.png"))
        # self.dojaSprite.walk_right_textures.append(arcade.load_texture("sprites/Doja/doja_walking_3.png"))
        # self.dojaSprite.walk_right_textures.append(arcade.load_texture("sprites/Doja/doja_walking_4.png"))
        # self.dojaSprite.walk_left_textures = []
        # self.dojaSprite.walk_left_textures.append(arcade.load_texture("sprites/Doja/doja_walking_0.png", mirrored=True))
        # self.dojaSprite.walk_left_textures.append(arcade.load_texture("sprites/Doja/doja_walking_1.png", mirrored=True))
        # self.dojaSprite.walk_left_textures.append(arcade.load_texture("sprites/Doja/doja_walking_2.png", mirrored=True))
        # self.dojaSprite.walk_left_textures.append(arcade.load_texture("sprites/Doja/doja_walking_3.png", mirrored=True))
        # self.dojaSprite.walk_left_textures.append(arcade.load_texture("sprites/Doja/doja_walking_4.png", mirrored=True))

        # Reads map level
        levelName = "level_1.tmx"
        sandLayer, miceLayer, cartonLayer, cactusLayer = 'Sand', 'Mice', 'Milk', 'Cactus'
        level = arcade.tilemap.read_tmx(levelName)

        # Tracks scrolling
        self.bottomView, self.leftView = 0, 0
        self.mapEnd = 64 * level.map_size                  # Calculate right edge of map in pixels

        # Reads each layer and puts each tile into a list
        self.sandList = arcade.tilemap.process_layer(level, sandLayer, tileScaling)
        self.miceList = arcade.tilemap.process_layer(level, miceLayer, tileScaling)
        self.milkList = arcade.tilemap.process_layer(level, cartonLayer, tileScaling)
        self.cactusList = arcade.tilemap.process_layer(level, cactusLayer, tileScaling)

        # Tracks score
        self.score = 0
        self.scoreSprite = arcade.load_texture("sprites/Mice/mice.png")

        # Tracks health
        self.health = 3
        self.healthSprite = arcade.load_texture("sprites/Milk/carton.png")

        # Load textures for menu and game over
        self.startText = arcade.load_texture("sprites/Texts/start.png")
        self.gameOverText = arcade.load_texture("sprites/Texts/gameover.png")
        self.restartText = arcade.load_texture("sprites/Texts/restart.png")

        # Sets up the physics of the game
        self.physicsDoja = arcade.PhysicsEnginePlatformer(self.dojaSprite, self.sandList, gravity)

    #def play_sounds(self):
        #if self.currentState == gameRunning:
            #arcade.play_sound(self.backgroundMusic)

    def draw_game_menu(self):
        startText = self.startText
        arcade.draw_texture_rectangle(screenWidth // 2, screenHeight // 2, 500, 40, startText, 0)

    def draw_game_over(self):
        gameOverText = self.gameOverText
        arcade.draw_texture_rectangle(self.leftView // 2, self.bottomView // 2, 70, 40, gameOverText, 0)
        restartText = self.restartText
        arcade.draw_texture_rectangle(self.leftView // 2, (self.bottomView // 2) - 50, 100, 40, restartText, 0)

    def draw_main_game(self):
        # Set background colour
        arcade.set_background_color((135, 206, 235))

        # Draw sprites
        self.sandList.draw()
        self.dojaList.draw()
        self.miceList.draw()
        self.milkList.draw()
        self.cactusList.draw()

        # Draw score
        scoreDisplay = f"     : {self.score}"
        arcade.draw_text(scoreDisplay, 10 + self.leftView, 520 + self.bottomView, arcade.csscolor.LIGHT_GRAY, 16)
        scoreSprite = self.scoreSprite
        arcade.draw_texture_rectangle(18 + self.leftView, 530 + self.bottomView, 40, 40, scoreSprite, 0)

        # Draw health
        healthDisplay = f"     : {self.health}"
        arcade.draw_text(healthDisplay, 10 + self.leftView, 480 + self.bottomView, arcade.csscolor.DARK_CYAN, 16)
        healthSprite = self.healthSprite
        arcade.draw_texture_rectangle(18 + self.leftView, 490 + self.bottomView, 30, 30, healthSprite, 0)

    def on_draw(self):
        # Sets background colour
        arcade.start_render()
        if self.currentState == gameMenu:
            self.draw_main_game()
            self.draw_game_menu()
        elif self.currentState == gameRunning:
            #self.play_sounds()
            self.draw_main_game()
        else:
            self.draw_main_game()
            self.draw_game_over()


    def on_key_press(self, key, modifiers):

        """Called when a key is pressed"""
        if self.currentState == gameMenu:
            if key == arcade.key.ENTER:
                self.currentState = gameRunning
        elif self.currentState == gameRunning:
            if key == arcade.key.UP or key == arcade.key.W:
                self.pressUp = True
            elif key == arcade.key.DOWN or key == arcade.key.S:
                self.pressDown = True
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.pressRight = True
            elif key == arcade.key.LEFT or key == arcade.key.A:
                self.pressLeft = True
        else:
            if key == arcade.key.P:
                self.currentState = gameRunning

    def on_key_release(self, key, modifiers):

        """Called when a key is released"""
        if key == arcade.key.UP or key == arcade.key.W:
            self.pressUp = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.pressDown = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.pressRight = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.pressLeft = False

    def on_update(self, delta_time): # delta_time creates speeds in pixel per second instead of per frame

        # Update the physics so dojaSprite moves
        self.physicsDoja.update()

        # Check for collisions
        miceEatenList = arcade.check_for_collision_with_list(self.dojaSprite, self.miceList)
        for mice in miceEatenList:
            mice.remove_from_sprite_lists()
            arcade.play_sound(self.miceEatenSound)
            self.score += 1

        milkDrankList = arcade.check_for_collision_with_list(self.dojaSprite, self.milkList)
        for milk in milkDrankList:
            milk.remove_from_sprite_lists()
            arcade.play_sound(self.milkSound)
            if self.health < 3:
                self.health += 1

        cactusHitList = arcade.check_for_collision_with_list(self.dojaSprite, self.cactusList)
        for cactus in cactusHitList:
            cactus.remove_from_sprite_lists()
            arcade.play_sound(self.cactusSound)
            self.health -= 1


        self.dojaSprite.change_x, self.dojaSprite.change_y = 0, 0
        if self.pressUp and not self.pressDown:
            if self.physicsDoja.can_jump():
                arcade.play_sound(self.jumpSound)
                self.dojaSprite.change_y = jumpSpeed
        elif self.pressDown and not self.pressUp:
            self.dojaSprite.change_y = -moveSpeed
        elif self.pressRight and not self.pressLeft:
            self.dojaSprite.change_x = moveSpeed
        elif self.pressLeft and not self.pressRight:
            self.dojaSprite.change_x = -moveSpeed

        # Updates if needed to scroll to any side
        scroll = False
        topBorder = self.bottomView + screenHeight - topMargin
        if self.dojaSprite.top > topBorder:
            self.bottomView += self.dojaSprite.top - topBorder
            scroll = True

        bottomBorder = self.bottomView + bottomMargin
        if self.dojaSprite.bottom < bottomBorder:
            self.bottomView -= bottomBorder - self.dojaSprite.bottom
            scroll = True

        rightBorder = self.leftView + screenWidth - rightMargin
        if self.dojaSprite.right > rightBorder:
            self.leftView += self.dojaSprite.right - rightBorder
            scroll = True

        leftBorder = self.leftView + leftMargin
        if self.dojaSprite.left < leftBorder:
            self.leftView -= leftBorder - self.dojaSprite.left
            scroll = True

        if scroll:
            self.bottomView = int(self.bottomView)
            self.leftView = int(self.leftView)
            # Scrolls
            arcade.set_viewport(self.leftView, screenWidth + self.leftView, self.bottomView, screenHeight + self.bottomView)

        # Returns Doja to the beginning if she falls of the map
        if self.dojaSprite.bottom == -300:
            if self.health <= 3:
                self.health -= 1
                self.dojaSprite.center_x, self.dojaSprite.center_y = 100, 100

        if self.health == -1:
            # PLAY GAME OVER MUSIC AFTER FALLING SOUND
            # arcade.stop_sound(self.backgroundMusic)
            self.bottomView = -300 # Stops the camera to scroll
            self.leftView = self.leftView
            self.dojaSprite.center_x, self.dojaSprite.center_y = 100, 100
            # Change game's state
            self.currentState = gameOver


def main():
    game = Feline(screenWidth, screenHeight, "Feline")
    game.setup()
    arcade.run()

main()