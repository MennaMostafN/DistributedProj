import pygame
import subprocess

pygame.init()

# Set the screen dimensions and create the screen surface
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


def draw_initial_screen():
    screen.fill((255, 255, 255))  # Clear the screen

    # Load the background image
    background_image = pygame.image.load("images/Picture1.png")

    # Scale the background image to fit the screen dimensions
    background_image = pygame.transform.scale(
        background_image, (screen_width, screen_height)
    )

    screen.blit(background_image, (0, 0))

    # Define button rectangles
    single_button_rect = pygame.Rect(200, 200, 400, 100)
    multiplayer_button_rect = pygame.Rect(200, 350, 400, 100)

    # Render button texts
    font = pygame.font.Font(None, 40)
    single_text = font.render("Single Player", True, (0, 0, 0))
    multiplayer_text = font.render("Multiplayer", True, (0, 0, 0))

    # Center the button texts within the button rectangles
    single_text_rect = single_text.get_rect(center=single_button_rect.center)
    multiplayer_text_rect = multiplayer_text.get_rect(
        center=multiplayer_button_rect.center
    )

    # Draw buttons and texts
    pygame.draw.rect(screen, (128, 0, 128), single_button_rect)
    pygame.draw.rect(screen, (128, 0, 128), multiplayer_button_rect)
    screen.blit(single_text, single_text_rect)
    screen.blit(multiplayer_text, multiplayer_text_rect)
    

    pygame.display.update()


def single_player_mode():
    pygame.quit()
    # Run the carRacingGame.py file as a subprocess
    subprocess.call(["python", "Singleplayer.py"])


def multiplayer_mode():
    pygame.quit()
    subprocess.call(["python", "Client.py"])


def main():
    draw_initial_screen()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                single_button_rect = pygame.Rect(200, 200, 400, 100)
                multiplayer_button_rect = pygame.Rect(200, 350, 400, 100)

                if single_button_rect.collidepoint(mouse_pos):
                    single_player_mode()
                    return
                elif multiplayer_button_rect.collidepoint(mouse_pos):
                    multiplayer_mode()
                    return

        pygame.time.Clock().tick(60)


main()
