import sys
import pygame
pygame.init()
pygame.display.set_caption("Abhay Nath")
from implementation import WIDTH, HEIGHT, FPS
from implementation import Player, Block, Block_1, Block_2, Block_3, Fire, get_background, draw, handle_move
from Levels.level_2 import lvl_2

def display_popup_message(message, window):
    font = pygame.font.Font(None, 96)
    text = font.render(message, True, (235, 64, 52))
    text_rect = text.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2)
    window.fill((255, 255, 255))
    window.blit(text, text_rect)
    pygame.display.flip()

def lvl_1(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")
    block_size = 96
    player = Player(100, 100, 50, 50)       #100,100,50,50

    fire = Fire(510, HEIGHT - block_size - 324, 16, 32)
    fire1 = Fire(1110, HEIGHT - block_size - 64, 16, 32)
    fire2 = Fire(1510, HEIGHT - block_size - 324, 16, 32)
    
    fire.on(),fire1.on(),fire2.on()

    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             #for i in range(-WIDTH // block_size, (WIDTH * 5) // block_size)]
             for i in range(47)]
    floor_1 = [Block(i * block_size, HEIGHT - block_size, block_size)
             #for i in range(-WIDTH // block_size, (WIDTH * 5) // block_size)]
             for i in range(49,64)]
    floor_2 = [Block(i * block_size, HEIGHT - block_size, block_size)
             #for i in range(-WIDTH // block_size, (WIDTH * 5) // block_size)]
             for i in range(68,139)]
    floor_3 = [Block(i * block_size, HEIGHT - block_size, block_size)
             #for i in range(-WIDTH // block_size, (WIDTH * 5) // block_size)]
             for i in range(141,200)]
    display_popup_message("Level 1", window)
    pygame.time.delay(2000)
    run = False
    objects = [*floor,Block(block_size * 4, HEIGHT - block_size * 3.7, block_size),fire,fire1,fire2,
               Block(block_size * 8, HEIGHT - block_size * 3.7, block_size),
               Block_1(block_size * 9, HEIGHT - block_size * 3.7, block_size),
               Block(block_size * 10, HEIGHT - block_size * 3.7, block_size),
               Block_1(block_size * 11, HEIGHT - block_size * 3.7, block_size),
               Block(block_size * 12, HEIGHT - block_size * 3.7, block_size),
               Block_1(block_size * 10, HEIGHT - block_size * 6.7, block_size),
               Block_2(block_size * 16, HEIGHT - block_size * 2, block_size),
               Block_2(block_size * 24, HEIGHT - block_size * 2, block_size),
               Block_2(block_size * 24, HEIGHT - block_size * 2.5, block_size),
               
               Block_2(block_size * 30, HEIGHT - block_size * 2, block_size),
               Block_2(block_size * 30, HEIGHT - block_size * 2.5, block_size),
               Block_2(block_size * 30, HEIGHT - block_size * 3, block_size),

               Block_2(block_size * 36, HEIGHT - block_size * 2, block_size),
               Block_2(block_size * 36, HEIGHT - block_size * 2.5, block_size),
               Block_2(block_size * 36, HEIGHT - block_size * 3, block_size),*floor_1,

               Block(block_size * 54, HEIGHT - block_size * 3.2, block_size),
               Block_1(block_size * 55, HEIGHT - block_size * 3.2, block_size),
               Block(block_size * 56, HEIGHT - block_size * 3.2, block_size),

               Block(block_size * 57, HEIGHT - block_size * 5.8, block_size),
               Block(block_size * 58, HEIGHT - block_size * 5.8, block_size),
               Block(block_size * 59, HEIGHT - block_size * 5.8, block_size),
               Block(block_size * 60, HEIGHT - block_size * 5.8, block_size),
               Block(block_size * 61, HEIGHT - block_size * 5.8, block_size),
               Block(block_size * 62, HEIGHT - block_size * 5.8, block_size),
               Block(block_size * 63, HEIGHT - block_size * 5.8, block_size),
               Block(block_size * 64, HEIGHT - block_size * 5.8, block_size),
               Block(block_size * 65, HEIGHT - block_size * 5.8, block_size),
               Block(block_size * 66, HEIGHT - block_size * 5.8, block_size),*floor_2,
               
               Block(block_size * 69, HEIGHT - block_size * 5.8, block_size),
               Block(block_size * 70, HEIGHT - block_size * 5.8, block_size),
               Block(block_size * 71, HEIGHT - block_size * 5.8, block_size),
               Block_1(block_size * 72, HEIGHT - block_size * 5.8, block_size),
               Block(block_size * 72, HEIGHT - block_size * 3.2, block_size),

               Block(block_size * 78, HEIGHT - block_size * 3.2, block_size),
               Block(block_size * 79, HEIGHT - block_size * 3.2, block_size),

               Block_1(block_size * 84, HEIGHT - block_size * 3.2, block_size),
               Block_1(block_size * 87, HEIGHT - block_size * 3.2, block_size),
               Block_1(block_size * 90, HEIGHT - block_size * 3.2, block_size),
               Block_1(block_size * 87, HEIGHT - block_size * 5.8, block_size),

               Block(block_size * 96, HEIGHT - block_size * 3.2, block_size),

               Block(block_size * 99, HEIGHT - block_size * 5.8, block_size),
               Block(block_size * 100, HEIGHT - block_size * 5.8, block_size),
               Block(block_size * 101, HEIGHT - block_size * 5.8, block_size),

               Block(block_size * 109, HEIGHT - block_size * 5.8, block_size),
               Block_1(block_size * 110, HEIGHT - block_size * 5.8, block_size),
               Block_1(block_size * 111, HEIGHT - block_size * 5.8, block_size),
               Block(block_size * 112, HEIGHT - block_size * 5.8, block_size),
               Block(block_size * 110, HEIGHT - block_size * 3.2, block_size),
               Block(block_size * 111, HEIGHT - block_size * 3.2, block_size),

               Block_3(block_size * 119, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 120, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 120, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 121, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 121, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 121, HEIGHT - block_size * 2.97, block_size),
               Block_3(block_size * 122, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 122, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 122, HEIGHT - block_size * 2.97, block_size),
               Block_3(block_size * 122, HEIGHT - block_size * 3.63, block_size),

               Block_3(block_size * 125, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 125, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 125, HEIGHT - block_size * 2.97, block_size),
               Block_3(block_size * 125, HEIGHT - block_size * 3.63, block_size),
               Block_3(block_size * 126, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 126, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 126, HEIGHT - block_size * 2.97, block_size),
               Block_3(block_size * 127, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 127, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 128, HEIGHT - block_size * 1.65, block_size),

               Block_3(block_size * 135, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 136, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 136, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 137, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 137, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 137, HEIGHT - block_size * 2.97, block_size),
               Block_3(block_size * 138, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 138, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 138, HEIGHT - block_size * 2.97, block_size),
               Block_3(block_size * 138, HEIGHT - block_size * 3.63, block_size),*floor_3,

               Block_3(block_size * 141, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 141, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 141, HEIGHT - block_size * 2.97, block_size),
               Block_3(block_size * 141, HEIGHT - block_size * 3.63, block_size),
               Block_3(block_size * 142, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 142, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 142, HEIGHT - block_size * 2.97, block_size),
               Block_3(block_size * 143, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 143, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 144, HEIGHT - block_size * 1.65, block_size),

               Block_2(block_size * 151, HEIGHT - block_size * 2, block_size),

               Block(block_size * 158, HEIGHT - block_size * 3.2, block_size),
               Block(block_size * 159, HEIGHT - block_size * 3.2, block_size),
               Block_1(block_size * 160, HEIGHT - block_size * 3.2, block_size),
               Block(block_size * 161, HEIGHT - block_size * 3.2, block_size),

               Block_2(block_size * 167, HEIGHT - block_size * 2, block_size),

               Block_3(block_size * 168, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 169, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 169, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 170, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 170, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 170, HEIGHT - block_size * 2.97, block_size),
               Block_3(block_size * 171, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 171, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 171, HEIGHT - block_size * 2.97, block_size),
               Block_3(block_size * 171, HEIGHT - block_size * 3.63, block_size),
               Block_3(block_size * 172, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 172, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 172, HEIGHT - block_size * 2.97, block_size),
               Block_3(block_size * 172, HEIGHT - block_size * 3.63, block_size),
               Block_3(block_size * 172, HEIGHT - block_size * 4.29, block_size),
               Block_3(block_size * 173, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 173, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 173, HEIGHT - block_size * 2.97, block_size),
               Block_3(block_size * 173, HEIGHT - block_size * 3.63, block_size),
               Block_3(block_size * 173, HEIGHT - block_size * 4.29, block_size),
               Block_3(block_size * 173, HEIGHT - block_size * 4.95, block_size),
               Block_3(block_size * 174, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 174, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 174, HEIGHT - block_size * 2.97, block_size),
               Block_3(block_size * 174, HEIGHT - block_size * 3.63, block_size),
               Block_3(block_size * 174, HEIGHT - block_size * 4.29, block_size),
               Block_3(block_size * 174, HEIGHT - block_size * 4.95, block_size),
               Block_3(block_size * 174, HEIGHT - block_size * 5.61, block_size),
               Block_3(block_size * 175, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 175, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 175, HEIGHT - block_size * 2.97, block_size),
               Block_3(block_size * 175, HEIGHT - block_size * 3.63, block_size),
               Block_3(block_size * 175, HEIGHT - block_size * 4.29, block_size),
               Block_3(block_size * 175, HEIGHT - block_size * 4.95, block_size),
               Block_3(block_size * 175, HEIGHT - block_size * 5.61, block_size),
               Block_3(block_size * 175, HEIGHT - block_size * 6.27, block_size),
               Block_3(block_size * 176, HEIGHT - block_size * 1.65, block_size),
               Block_3(block_size * 176, HEIGHT - block_size * 2.31, block_size),
               Block_3(block_size * 176, HEIGHT - block_size * 2.97, block_size),
               Block_3(block_size * 176, HEIGHT - block_size * 3.63, block_size),
               Block_3(block_size * 176, HEIGHT - block_size * 4.29, block_size),
               Block_3(block_size * 176, HEIGHT - block_size * 4.95, block_size),
               Block_3(block_size * 176, HEIGHT - block_size * 5.61, block_size),
               Block_3(block_size * 176, HEIGHT - block_size * 6.27, block_size),

               Block_3(block_size * 182, HEIGHT - block_size * 1.65, block_size),
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
            if offset_x == 16933:    #16933
                display_popup_message("Level 1 Completed!", window)
                pygame.time.delay(4000)
                run = False
                lvl_2(window)

    pygame.quit()
    quit()