import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("laba_game")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = True

sky_surf = pygame.image.load('/home/aziz/vs/game/sky.png').convert()
ground_surf = pygame.image.load('/home/aziz/vs/game/ground.png').convert()

score_surf = test_font.render('My game', True, (200, 0, 0))
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('/home/aziz/vs/game/snail.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (900, 300))

player_surf = pygame.image.load('/home/aziz/vs/game/player1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (50, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                        player_gravity = -20 
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.left = 800

    if game_active:
        screen.blit(sky_surf,(0, 0))
        screen.blit(ground_surf,(0, 300))
        #pygame.draw.rect(screen,(33, 33, 33),score_rect,10)
        #pygame.draw.rect(screen,(33, 33, 33),score_rect)
        screen.blit(score_surf,score_rect)
        
        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail_surf,snail_rect)
        
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >=  300: 
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        keys = pygame.key.get_pressed()

        if player_rect.colliderect(snail_rect):
            game_active = False
    else:
        screen.fill('Yellow')

    pygame.display.update()
    clock.tick(60)
