#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 22:56:36 2024

@author: caleernsberger
"""

import pygame
import random
import time

class Block(pygame.sprite.Sprite):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene
       
        original_image = pygame.image.load("Charlie.png").convert_alpha()
        self.image = pygame.transform.scale(original_image, (50, 50)) 
        self.rect = self.image.get_rect()
        self.rect.centerx = scene.screen.get_width() // 2
        self.rect.bottom = scene.screen.get_height() - 10
        self.speed = 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < self.scene.screen.get_width():
            self.rect.x += self.speed


class Wall(pygame.sprite.Sprite):
    def __init__(self, scene, x, y, gap_x):
        super().__init__()
        self.scene = scene
        wall_length = scene.screen.get_width() // 5  
        self.image = pygame.Surface((wall_length, 20))
        self.image.fill((255, 255, 255))
        
        spike_height = 40
        num_spikes = int(self.image.get_width() / 10)  # Number of spikes based on wall width
        for i in range(num_spikes):
            pygame.draw.polygon(self.image, (255, 0, 0),
                                [(i * 20, 20), (i * 20 + 10, 20), (i * 20 + 20, 0)])
        # Create a gap in the spikes where the block can pass
        pygame.draw.rect(self.image, (255, 255, 255), pygame.Rect(gap_x, 0, 200, spike_height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.gap_x = gap_x
        self.gap_width = 200

    def update(self):
        self.rect.y += 5  # Increase the speed to make walls fall faster
        if self.rect.top > self.scene.screen.get_height():
            self.kill()

class Coin(pygame.sprite.Sprite):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene
        # Load the .png image and resize it
        original_image = pygame.image.load("coin.png").convert_alpha()
        self.image = pygame.transform.scale(original_image, (25, 25))  # Resize to (25, 25)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0, scene.screen.get_width())
        self.rect.bottom = 0
        self.speed = random.randint(5, 5)
        self.creation_time = time.time()

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.scene.screen.get_height():
            self.rect.centerx = random.randint(0, self.scene.screen.get_width())
            self.rect.bottom = 0
            self.speed = random.randint(2, 5)
            self.creation_time = time.time()

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("coin-dash/dodge")

        # Load background image
        self.background_image = pygame.image.load("sky2.jpg").convert()

        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()

        self.block = Block(self)
        self.all_sprites.add(self.block)

        self.score = 0
        self.score_font = pygame.font.SysFont(None, 36)

        self.start_time = time.time()  # Start time for the game
        self.game_over_time = None 

        self.timer_font = pygame.font.SysFont(None, 36)
        self.game_over_font = pygame.font.SysFont(None, 72)

        # Define levels
        self.levels = [
            {"wall_frequency": 3, "coin_creation_interval": 0.8},
            {"wall_frequency": 5, "coin_creation_interval": 0.6},
            {"wall_frequency": 7, "coin_creation_interval": 0.4}
        ]
        self.current_level = 0

        self.wall_timer = 0
        self.coin_timer = time.time()

        self.passed_wall = False  

        self.running = True
        self.game_over = False

    def create_wall(self):
        gap_x = random.randint(0, self.screen_width - 200)  
        wall_x = random.randint(0, self.screen_width - self.screen_width // 5)  # Randomize wall position
        wall = Wall(self, wall_x, -20, gap_x)
        self.all_sprites.add(wall)
        self.walls.add(wall)

    def create_coin(self):
        if time.time() - self.coin_timer >= self.levels[self.current_level]["coin_creation_interval"]:
            coin = Coin(self)
            self.all_sprites.add(coin)
            self.coins.add(coin)
            self.coin_timer = time.time()

    def restart_game(self):
        self.all_sprites.empty()
        self.walls.empty()
        self.coins.empty()

        self.block = Block(self)
        self.all_sprites.add(self.block)

        self.score = 0
        self.start_time = time.time()  # Restart timer
        self.current_level = 0
        self.wall_timer = 0
        self.coin_timer = time.time()
        self.passed_wall = False
        self.game_over = False
        self.game_over_time = None

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and self.game_over:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.restart_button_rect.collidepoint(mouse_pos):
                        self.restart_game()

            if not self.game_over:
                self.all_sprites.update()

                hits = pygame.sprite.spritecollide(self.block, self.walls, False)
                if hits:
                    self.game_over = True
                    self.game_over_time = time.time() - self.start_time

                coin_hits = pygame.sprite.spritecollide(self.block, self.coins, True)
                if coin_hits:
                    self.score += 1

                walls_to_remove = [wall for wall in self.walls if wall.rect.top > self.screen_height]
                for wall in walls_to_remove:
                    self.walls.remove(wall)
                    self.all_sprites.remove(wall)

                coins_to_remove = [coin for coin in self.coins if coin.rect.top > self.screen_height]
                for coin in coins_to_remove:
                    self.coins.remove(coin)
                    self.all_sprites.remove(coin)

                if random.random() < self.levels[self.current_level]["wall_frequency"] / 60:  # Adjusted for 60 FPS
                    self.create_wall()

                if time.time() - self.wall_timer >= 1 / self.levels[self.current_level]["wall_frequency"] and not self.passed_wall:
                    self.score += 1  
                    self.wall_timer = time.time()  # Reset wall timer
                    self.passed_wall = True  

                self.create_coin()

                
                self.screen.blit(self.background_image, (0, 0))

                self.all_sprites.draw(self.screen)
                score_text = self.score_font.render("Score: " + str(self.score), True, (255, 255, 255))
                self.screen.blit(score_text, (10, 10))

                
                elapsed_time = time.time() - self.start_time
                timer_text = self.timer_font.render("Time: {:.1f}".format(elapsed_time), True, (255, 255, 255))
                self.screen.blit(timer_text, (10, 50))  

            if self.game_over:
                self.display_game_over()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def display_game_over(self):
        final_score_text = self.game_over_font.render("Game Over", True, (255, 0, 0))
        self.screen.blit(final_score_text, (self.screen_width // 2 - 140, self.screen_height // 2 - 50))

        score_text = self.score_font.render("Final Score: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(score_text, (self.screen_width // 2 - 90, self.screen_height // 2 + 20))

        if self.game_over_time is not None:
            final_time_text = self.score_font.render("Time: {:.1f}".format(self.game_over_time), True, (255, 255, 255))
            self.screen.blit(final_time_text, (self.screen_width // 2 - 60, self.screen_height // 2 + 60))

        
        restart_text = self.score_font.render("Restart", True, (255, 255, 255))
        restart_button_width = 150
        restart_button_height = 50
        restart_button_x = self.screen_width // 2 - restart_button_width // 2
        restart_button_y = self.screen_height // 2 + 100
        self.restart_button_rect = pygame.Rect(restart_button_x, restart_button_y, restart_button_width, restart_button_height)
        pygame.draw.rect(self.screen, (0, 255, 0), self.restart_button_rect)
        self.screen.blit(restart_text, (restart_button_x + 30, restart_button_y + 10))
def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
