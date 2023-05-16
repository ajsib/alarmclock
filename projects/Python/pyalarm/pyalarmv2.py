import pygame
import datetime
import time
import os
import sys
import tkinter as tk
import tkinter.ttk as ttk

class AlarmApp:
    def __init__(self, master):
        self.master = master
        master.title("Alarm App")
        master.geometry("400x300")

        # Set up the style for the widgets
        style = ttk.Style()
        style.configure('TLabel', font=('Segoe UI', 14), padding=10)
        style.configure('TEntry', font=('Segoe UI', 14), padding=10)
        style.configure('TButton', font=('Segoe UI', 14), padding=10)

        # Create labels and entry fields for user input
        self.hour_label = ttk.Label(master, text="Hour:")
        self.hour_label.grid(row=0, column=0, sticky="W")
        self.hour_entry = ttk.Entry(master, width=5)
        self.hour_entry.grid(row=0, column=1, sticky="E")

        self.minute_label = ttk.Label(master, text="Minute:")
        self.minute_label.grid(row=1, column=0, sticky="W")
        self.minute_entry = ttk.Entry(master, width=5)
        self.minute_entry.grid(row=1, column=1, sticky="E")

        self.volume_label = ttk.Label(master, text="Volume Increase (%):")
        self.volume_label.grid(row=2, column=0, sticky="W")
        self.volume_entry = ttk.Entry(master, width=5)
        self.volume_entry.grid(row=2, column=1, sticky="E")

        # Create a button to set the alarm
        self.set_button = ttk.Button(master, text="Set Alarm", command=self.set_alarm)
        self.set_button.grid(row=3, column=0, columnspan=2, pady=20)

        # Initialize Pygame
        pygame.mixer.init()

        # Load the MP3 file
        pygame.mixer.music.load('./SSRO.mp3')

    def set_alarm(self):
        # Get user input
        hourin = int(self.hour_entry.get())
        minutein = int(self.minute_entry.get())
        volumein = int(self.volume_entry.get())

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

    def close(self):
        # Clean up Pygame
        pygame.mixer.quit()
        self.master.destroy()

root = tk.Tk()
app = AlarmApp(root)
root.protocol("WM_DELETE_WINDOW", app.close)
root.mainloop()
