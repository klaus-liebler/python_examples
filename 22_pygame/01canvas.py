import pygame
def create_board():
    cellSize = 80
    board = pygame.Surface((cellSize * 8, cellSize * 8))
    board.fill((255, 255, 255))
    for x in range(8):
        for y in range(8):
            if (x+y)%2==1:
                pygame.draw.rect(board, (0,0,0), (x*cellSize, y*cellSize, cellSize, cellSize))
    return board
pygame.init()
board = create_board()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Bunny Mover")
bunny =pygame.image.load("bunny80.png").convert_alpha()
clock = pygame.time.Clock()

def update_bunny_on_screen():
    screen.blit(board, board.get_rect())
    screen.blit(bunny, bunny_pos)
    pygame.display.flip()
    clock.tick(60)


running = True
dt = 0

bunny_pos = pygame.Vector2(0, 0)
while bunny_pos.x<320:
    bunny_pos.x = bunny_pos.x+1
    update_bunny_on_screen()

while bunny_pos.y<160:
    bunny_pos.y = bunny_pos.y+1
    update_bunny_on_screen()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()