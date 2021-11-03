import pygame

# GAME
icon = pygame.image.load('./assets/bob.png')
pygame.display.set_icon(icon)

pygame.display.set_caption('bob')
screen = pygame.display.set_mode((800, 900))

# DHAR
dhar = pygame.image.load('./assets/9k.png')
dhar = pygame.transform.scale(dhar, (100, 150))
#                  position  size
mann = pygame.Rect(350, 422, 100, 150)

def images():
    background = pygame.image.load('./assets/background.png')
    screen.blit(background, (0, 0))

    # MUSIC
    man = pygame.image.load('./assets/man.png')
    man = pygame.transform.scale(man, (800, 900))
    man.set_alpha(0)
    if mann.y < 50:
        man.set_alpha(255)
        pygame.mixer.music.stop()
        pygame.mixer.music.load('./assets/boom.wav')
        pygame.mixer.music.play()
    screen.blit(man, (0, 0))


def keybinds():
    # DHAR
    if mann.y < 422:
        mann.y += 50

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] and mann.y > 50:
        mann.y -= 100
    if keys_pressed[pygame.K_RIGHT] and mann.x < 700:
        mann.x += 10
    if keys_pressed[pygame.K_LEFT] and mann.x > 0:
        mann.x -= 10
    
    screen.blit(dhar, (mann.x, mann.y))


def main():
    pygame.init()
    pygame.mixer.music.load('./assets/pullup.wav')
    pygame.mixer.music.play(-1) 

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        images()
        keybinds()
        pygame.display.flip()

if __name__ == "__main__":
    main()