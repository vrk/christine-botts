from gpiozero import Button
import pygame
import random
import os


pygame.init()

button = Button(2)


while True:
    if button.is_pressed:
        print("Button is pressed")
        # Get random audio
        directory_path = '/home/vrk/christine-botts/test-audio'
        file_list = os.listdir(directory_path)
        random_file= random.choice(file_list)
        print(random_file)

        # Play sound
        my_sound = pygame.mixer.Sound('test-audio/' + random_file)
        my_sound.play()

        # Block while playing
        while (pygame.mixer.Channel(0).get_busy() == True):
            print("playing a sound");
        print("done")


