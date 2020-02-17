import pygame
pygame.init()
x = 0
x1 = 130
y = 0
hp = 100

win = pygame.display.set_mode((800, 600))
img = pygame.image.load('assets/gfx/fireflies.png')
img2 = pygame.image.load('assets/gfx/paper.jpg')
img3 = pygame.image.load('assets/gfx/vault.png')
img4 = pygame.image.load('assets/gfx/paper2.jpg')
img5 = pygame.image.load('assets/gfx/deagle.png')
img6 = pygame.image.load('assets/hero/sliced/idle-1.png')
img6 = pygame.transform.scale(img6, (64,64))
img7 = pygame.image.load('assets/forest-assets/cave.png')


font = pygame.font.SysFont("arial", 72)
text1 = font.render("The Fireflies", True, (255, 255, 255))
font = pygame.font.SysFont("arial", 20)
text2 = font.render("By: Anthony", True, (255, 255, 255))
font = pygame.font.SysFont("arial", 21)
text3 = font.render("2020", True, (255, 255, 255))
font = pygame.font.SysFont("arial", 21)
text4 = font.render("HP: " + str(hp), True, (255, 255, 255))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    win.blit(img, (550, 0))
    win.blit(img2, (110, 150))
    win.blit(img3, (x1, 170))
    win.blit(img4, (110, 350))
    win.blit(img5, (130, 370))
    win.blit(img6, (x, y))
    
    
     
    win.blit(text1, (110, 0))
    win.blit(text2, (395, 70))
    win.blit(text3, (455, 95))

    # HP counter
    text4 = font.render("HP: " + str(hp), True, (255, 255, 255))
    win.blit(text4, (720, 570))

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 0.5
    if keys[pygame.K_RIGHT]:
        x += 0.5
    if keys[pygame.K_UP]:
        y -= 0.5
    if keys[pygame.K_DOWN]:
        y += 0.5
    if keys[pygame.K_a]:
        win.blit(img7, (130, 170))
        x1 = 500
        

    if x >= 800:
        hp -= 1
        print(hp)

    if x <= -15:
        hp -= 1
        print(hp)

    if x == 795:
        x = 0
        y = 0


    pygame.display.update()

pygame.quit()