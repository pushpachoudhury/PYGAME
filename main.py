import pygame

pygame.init() # how you call a method, initializing the game

display_width = 900 # 800 pixels wide
display_height = 600 # 600 pixels wide
gameDisplay = pygame.display.set_mode((display_width, display_height)) 
# ^ sets up game display

black = (0,0,0) # RGB color-code
white = (255, 255, 255)
blue = (0,0, 255)
font = pygame.font.Font(None, 36) # default font, 36 size

clock = pygame.time.Clock()

p1 = pygame.image.load('mario!.jpeg') # creates avatars that u can set an image to
p2 = pygame.image.load('bowser!.png')

p1_health = 100 # health for both avatars
p2_health = 100

p1_speed = 0 # sets speed
p2_speed = 0

# starting positions
p1_x_pos = (0)
p1_y_pos = (display_height -350 ) # may change based on avatar

p2_x_pos = (display_width - 275) # p2 would be all the way to the right
p2_y_pos = (display_height -350) # same level as p1

winner = '' # empty bc no winner yet 

running = True # want game to run

# while game is being played
while running:

  for event in pygame.event.get(): 
    # ^ pygame is receiving any event (user interaction)
    
    if event.type == pygame.KEYDOWN: #someone is pressing a key
      
    # sets left and right movements  
      if event.key == pygame.K_a: #K means 'key'
          p1_speed -= 10
      elif event.key == pygame.K_d:
         p1_speed += 10
      elif event.key == pygame.K_LEFT:
           p2_speed -= 10
      elif event.key == pygame.K_RIGHT:
          p2_speed += 10

#attack logic
      if p1_x_pos - p2_x_pos > -210 and p1_x_pos - p2_x_pos < 210: #if two pictures touch
        if event.key == pygame.K_e and p1_health > 0 and p2_health > 0:
          p2_health -= 10
        elif event.key == pygame.K_l and p1_health > 0 and p2_health > 0:
          p1_health -= 10
     
    elif event.type == pygame.KEYUP: #someone is releasing a key
      if event.key == pygame.K_a or event.key == pygame.K_d:
        p1_speed = 0
      elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        p2_speed = 0
      
  p1_x_pos += p1_speed # changes position 
  p2_x_pos += p2_speed

#health display
  p1_text = font.render("P1 Health: " + str(p1_health),True,black)
  p1_text_rect = p1_text.get_rect() # rectangle text will be in
  p1_text_rect.center = (150,100) # coordinates its going to be displayed at

  p2_text = font.render("P2 Health: " + str(p2_health),True,black)
  p2_text_rect = p2_text.get_rect() 
  p2_text_rect.center = (750,100)

#winner announcement
  if p1_health <= 0:
    winner = "P2 wins!"
  elif p2_health <= 0:
    winner = "P1 wins!"

#winner display
  winner_text = font.render(winner, True,black)
  winner_rect = winner_text.get_rect()
  winner_rect.center = (450,200)

  gameDisplay.fill(white)

#puts players on screen
  gameDisplay.blit(p1, (p1_x_pos, p1_y_pos))
  gameDisplay.blit(p2, (p2_x_pos, p2_y_pos))

  gameDisplay.blit(p1_text, p1_text_rect)
  gameDisplay.blit(p2_text, p2_text_rect)

  gameDisplay.blit(winner_text, winner_rect)
  
  pygame.display.update() # updates the screen

  clock.tick(30)
pygame.quit()
quit()
