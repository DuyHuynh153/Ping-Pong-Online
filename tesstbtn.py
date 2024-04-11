

import pygame

# Initialize pygame
pygame.init()


from Button import Button
# Set up the display
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Button Example")

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define a font
font = pygame.font.SysFont(None, 30)

# Create some buttons
button1 = Button(1, 100, 100, 20, 10, "Button 1", font, GREEN, RED, WHITE, BLACK, outline_width=2, outline_color=BLACK)
button2 = Button(2, 100, 200, 20, 10, "Button 2", font, RED, GREEN, WHITE, BLACK, outline_width=2, outline_color=BLACK)
button3 = Button(3, 100, 300, 20, 10, "Button 3", font, WHITE, BLACK, BLACK, WHITE, outline_width=2, outline_color=BLACK)

# List of buttons
buttons = [button1, button2, button3]

# Main loop
run = True
while run:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                for button in buttons:
                    if button.is_over(*event.pos):
                        print(f"Button {button.id} clicked!")

    # Drawing
    win.fill(WHITE)
    for button in buttons:
        button.draw(win)
    pygame.display.update()

pygame.quit()