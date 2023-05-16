import pygame
import datetime
import time
import os
import sys

args = sys.argv[1:]
hourin = int(args[0])
minutein = int(args[1])
volumein = int(args[2])

# Initialize Pygame
pygame.mixer.init()

# Load the MP3 file
pygame.mixer.music.load('./SSRO.mp3')

# Set the desired time to play the file (24-hour format)
play_time = datetime.time(hour=hourin, minute=minutein, second=0)

# Set the volume increase amount (in percent)
volume_increase = volumein

# Initialize the flag variable
file_played = False

# Loop until the file has been played
while True:
    # Get the current time
    now = datetime.datetime.now().time()

    # If the current time matches the desired play time and the file hasn't been played yet, increase the volume and play the file
    if now.hour == play_time.hour and now.minute == play_time.minute and now.second == play_time.second and not file_played:
        # Increase the volume using the amixer command
        os.system(f'amixer -D pulse sset Master {volume_increase}%+')

        # Play the file
        pygame.mixer.music.play()
        time.sleep(120)
        break

    # Wait for 1 second before checking the time again
    time.sleep(1)

# Clean up Pygame
pygame.mixer.quit()
