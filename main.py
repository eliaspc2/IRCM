# Complete your game here
import pygame
import random

class Constants:
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 420
    IMAGES = ["coin", "door", "monster", "robot"]
    PLAYER_SPEED = 5
    COIN_SPEED = 1
    ENEMY_SPEED = 2
    COIN_FREQUENCY = 14
    ENEMY_FREQUENCY = 7

class Player:
    def __init__(self, window, image):
        self.window = window
        self.image = image
        self.x = (Constants.WINDOW_WIDTH - self.image.get_width()) // 2
        self.x_limit = Constants.WINDOW_WIDTH - self.image.get_width()
        self.y = (Constants.WINDOW_HEIGHT - self.image.get_height()) - 30
        self.speed = Constants.PLAYER_SPEED
        self.mask = pygame.mask.from_surface(self.image) 

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

    def move(self, value):
        self.x += value
        if self.x > self.x_limit:
            self.x = self.x_limit
        elif self.x < 0:
            self.x = 0
    
    def get_overlaping_area(self, skin, offset_x, offset_y): 
        who_mask = pygame.mask.from_surface(skin) 
        return who_mask.overlap_area(self.mask, [self.x - offset_x, self.y - offset_y]) 
    
    def colides(self, who): 
        return who.get_overlaping_area(self.image, self.x, self.y) > 0

class Drop:
    def __init__(self, window, image, speed):
        self.window = window
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.x_limit = Constants.WINDOW_WIDTH - self.image.get_width()
        self.x = random.randint(0, self.x_limit)
        self.y = -self.image.get_height()
        self.y_limit = Constants.WINDOW_HEIGHT - self.image.get_height()
        self.speed = speed

    def get_overlaping_area(self, skin, offset_x, offset_y): 
        who_mask = pygame.mask.from_surface(skin) 
        return who_mask.overlap_area(self.mask, [self.x - offset_x, self.y - offset_y]) 
    
    def colides(self, who): 
        return who.get_overlaping_area(self.image, self.x, self.y) > 0

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

    def update(self, level):
        self.y += self.speed + level // 2
        if self.y >= self.y_limit:
            return True
        return False

class IRCM:
    def __init__(self):
        pygame.init()
        self.load_objects()
        self.window = pygame.display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
        pygame.display.set_caption("It’s Raining Coins and Monsters")
        self.clock = pygame.time.Clock()

        self.new_game()
        self.main_loop()

    def load_objects(self):
        self.game_font = pygame.font.SysFont("Arial", 24)
        self.images = {}
        for name in Constants.IMAGES:
            self.images[name] = pygame.image.load(name + ".png")

    def new_game(self):
        self.player = Player(self.window, self.images["robot"]) 
        self.score = 0
        self.game_over = False
        self.coins = []
        self.enemies = []
        self.frame_count = 0

    def game_over_scr(self):
        self.game_over = True
        self.game_over_text = self.game_font.render(f"GAME OVER", True, (255, 0, 0))

    def main_loop(self):
        while True:
            self.check_events()
            if not self.game_over:
                self.update_window()
            else:
                self.game_over_scr()
            self.draw_window()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_F2:
                    self.new_game()

        if self.game_over:
            return
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            self.player.move(Constants.PLAYER_SPEED)
        elif key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            self.player.move(-Constants.PLAYER_SPEED)

    def update_window(self):
        if self.frame_count < 900:
            self.frame_count += 1
            self.intro_text = self.game_font.render("Catch coins, avoid monsters", True, (255, 0, 0))
        self.footer_text = self.game_font.render("F2 = New Game   |   Esc = Exit Game", True, (255, 0, 0))
        self.text = self.game_font.render(f"Points: {self.score}", True, (255, 0, 0))

        level = max(0, self.score // 10)
        if random.randint(1, 1000) <= max(Constants.COIN_FREQUENCY - level, 1):
            self.coins.append(Drop(self.window, self.images["coin"], Constants.COIN_SPEED))
        if random.randint(1, 1000) <= min(Constants.ENEMY_FREQUENCY + level, 1000):
            self.enemies.append(Drop(self.window, self.images["monster"], Constants.ENEMY_SPEED))
        
        if self.coins:
            for coin in self.coins[:]:
                if coin.update(level):
                    self.coins.remove(coin)
                    self.score -= 1
                if coin.colides(self.player):
                    self.coins.remove(coin)
                    self.score += 1
        
        if self.enemies:
            for enemy in self.enemies[:]:
                if enemy.update(level):
                    self.enemies.remove(enemy)
                if enemy.colides(self.player):
                    self.game_over_scr()
                    
    def draw_window(self):
        self.window.fill((20, 20, 20))

        if self.frame_count < 900:
            x = (Constants.WINDOW_WIDTH - self.intro_text.get_width()) // 2
            self.window.blit(self.intro_text, (x, 100))
        self.player.draw()
        self.window.blit(self.text, (540, 20))
        self.window.blit(self.footer_text, (160, Constants.WINDOW_HEIGHT - 30))
        for coin in self.coins:
            coin.draw()
        for enemy in self.enemies:
            enemy.draw()
        if self.game_over:
            x = (Constants.WINDOW_WIDTH - self.game_over_text.get_width()) // 2
            self.window.blit(self.game_over_text, (x, 100))
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == "__main__":
    IRCM()