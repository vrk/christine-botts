from gpiozero import Button
import pygame

pygame.init()

button = Button(2)

while True:
    if button.is_pressed:
        print("Button is pressed")
        my_sound = pygame.mixer.Sound('test-audio/piano2.wav')
        my_sound.play()


