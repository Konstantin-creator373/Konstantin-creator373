import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('пакман')

font1 = pygame.font.Font(None, 80)
win = font1.render('Победа', 1, (0, 128, 0))


walls = [
    pygame.Rect(0, 0, 1000, 30),
    pygame.Rect(0, 670, 1000, 30),
    pygame.Rect(970, 0, 30, 1000),
    pygame.Rect(0, 0, 30, 1000),
    pygame.Rect(530, 70, 400, 300),
    pygame.Rect(80, 70, 400, 300),
    pygame.Rect(530, 410, 400, 230),
    pygame.Rect(80, 410, 400, 230)
]

tchk = [(505, 50, 3)]

clon_tchk = []
for i in [0, -50, -100, -150, -200, -250, -300, -350, -400, -450,
          50, 100, 150, 200, 250,
          300, 350, 400]:
    for i1 in [0, 335, 600]:
        for circle in tchk:
            x, y, radius = circle
            clon_tchk.append((x + i, y + i1, radius))

pacman = pygame.image.load('pacman.png')
pacman = pygame.transform.scale(pacman, (35, 25))

pacmanX = 490
pacmanY = 370

speed = 1
to_left = False
to_right = False
to_up = False
to_down = False

enemy = pygame.image.load("prizrak.png")
enemy = pygame.transform.scale(enemy, (40, 30))
enemy_rect = enemy.get_rect()
enemy_rect.y = 640

enemy2 = pygame.image.load("prizrak.png")
enemy2 = pygame.transform.scale(enemy2, (40, 30))
enemy_rect2 = enemy.get_rect()
enemy_rect2.y = 100
enemy_rect2.x = 930

enemy3 = pygame.image.load("prizrak.png")
enemy3 = pygame.transform.scale(enemy3, (40, 30))
enemy_rect3 = enemy.get_rect()
enemy_rect3.y = 40
enemy_rect3.x = 50

direction = 1
direction2 = 1
direction3 = 1

pygame.time.Clock().tick(1)

run = True

while run:
    screen.fill((0, 0, 0))

    enemy_rect.x += speed * direction
    enemy_rect2.y += speed * direction2
    enemy_rect3.x += speed * direction3

    if enemy_rect.x > 1000:
        direction = -1
    elif enemy_rect.x < -enemy_rect.width:
        direction = 1

    if enemy_rect3.x > 1000:
        direction3 = -1
    elif enemy_rect3.x < -enemy_rect3.width:
        direction3 = 1

    for wall in walls:
        pygame.draw.rect(screen, (25, 25, 112), wall)

    for circle in clon_tchk:
        x, y, radius = circle
        pygame.draw.circle(screen, (255, 255, 0), (x, y), radius)


    if enemy_rect2.y > 700:
        direction2 = -1
    elif enemy_rect2.y < -enemy_rect2.height:
        direction2 = 1

    for wall in walls:
        pygame.draw.rect(screen, (25, 25, 112), wall)

    for circle in clon_tchk:
        x, y, radius = circle
        pygame.draw.circle(screen, (255, 255, 0), (x, y), radius)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_DOWN:
                to_down = True
            if event.key == pygame.K_UP:
                to_up = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_DOWN:
                to_down = False
            if event.key == pygame.K_UP:
                to_up = False

        if event.type == pygame.QUIT:
            run = False

    hitbox = pygame.Rect(pacmanX, pacmanY, pacman.get_width(), pacman.get_height())

    if to_right:
        hitbox.x += speed
        if not any(hitbox.colliderect(wall) for wall in walls):
            pacmanX += speed

    if to_left:
        hitbox.x -= speed
        if not any(hitbox.colliderect(wall) for wall in walls):
            pacmanX -= speed

    if to_down:
        hitbox.y += speed
        if not any(hitbox.colliderect(wall) for wall in walls):
            pacmanY += speed

    if to_up:
        hitbox.y -= speed
        if not any(hitbox.colliderect(wall) for wall in walls):
            pacmanY -= speed

    for i in clon_tchk[:]:
        x, y, radius = i
        circle_rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)

        if hitbox.colliderect(circle_rect):
            clon_tchk.remove(i)

    screen.blit(pacman, (pacmanX, pacmanY))

    screen.blit(enemy, enemy_rect)

    screen.blit(enemy2, enemy_rect2)

    screen.blit(enemy3, enemy_rect3)

    if hitbox.colliderect(enemy_rect):
        run = False

    if hitbox.colliderect(enemy_rect2):
        run = False

    if hitbox.colliderect(enemy_rect3):
        run = False

    if not clon_tchk:
        screen.blit(win, (400, 350))
    pygame.display.update()

pygame.quit()
