import sys
import pygame
pygame.init()
pygame.display.set_caption("Abhay Nath")
from implementation import WIDTH, HEIGHT, FPS
from implementation import Player, Block, Block_1, Block_2, Block_3, Fire, get_background, draw, handle_move
#from Levels.level_2 import lvl_2

def display_popup_message(message, window):
    font = pygame.font.Font(None, 96)
    text = font.render(message, True, (235, 64, 52))
    text_rect = text.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2)
    window.fill((255, 255, 255))
    window.blit(text, text_rect)
    pygame.display.flip()

def lvl_2(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")
    block_size = 96
    player = Player(100, 550, 0, 0)       #100,550,50,50

    fire = Fire(510, HEIGHT - block_size - 324, 16, 32)
    fire1 = Fire(1110, HEIGHT - block_size - 64, 16, 32)
    fire2 = Fire(1510, HEIGHT - block_size - 324, 16, 32)
    
    fire.on(),fire1.on(),fire2.on()

    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             #for i in range(-WIDTH // block_size, (WIDTH * 5) // block_size)]
             for i in range(0,11)]
    floor_1 = [Block(i * block_size, HEIGHT - block_size, block_size)
             #for i in range(-WIDTH // block_size, (WIDTH * 5) // block_size)]
             for i in range(12,20)]
    # floor_2 = [Block(i * block_size, HEIGHT - block_size, block_size)
    #          #for i in range(-WIDTH // block_size, (WIDTH * 5) // block_size)]
    #          for i in range(68,139)]
    # floor_3 = [Block(i * block_size, HEIGHT - block_size, block_size)
    #          #for i in range(-WIDTH // block_size, (WIDTH * 5) // block_size)]
    #          for i in range(141,200)]
    display_popup_message("Level 2", window)
    pygame.time.delay(2000)
    run = False
    objects = [*floor,Block_2(block_size * 9, HEIGHT - block_size * 3, block_size),#fire,fire1,fire2,
               Block_2(block_size * 10, HEIGHT - block_size * 3, block_size),*floor_1,
               Block_2(block_size * 11, HEIGHT - block_size * 3, block_size),
               Block_2(block_size * 12, HEIGHT - block_size * 3, block_size),
               Block_2(block_size * 12, HEIGHT - block_size * 2, block_size),
               ]

    offset_x = 0         #0
    scroll_area_width = 900

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()

        player.loop(FPS)
        fire.loop(),fire1.loop(),fire2.loop()
        handle_move(player, objects)
        draw(window, background, bg_image, player, objects, offset_x)

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel
            offset_y = 0
            offset_y += player.y_vel
            if offset_x == 644 and offset_y == 1.2:    #644
                display_popup_message("Level 2 Completed!", window)
                pygame.time.delay(4000)
                run = False
                #lvl_2(window)

    pygame.quit()
    quit()