import pygame # import library
pygame.init()

# Create the window
win = pygame.display.set_mode((800, 600))

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

# Game code starts here ---------------------
  win.fill((0, 0, 0))

  img = pygame.image.load('character.png').convert

  win.blit(img, (400, 300))

  # Draw a rectangle
  pygame.draw.rect(win, (111, 204, 232), (50, 50, 100, 200))
  
  #Update the display
  pygame.display.update()

print("Ending game")
pygame.quit()
