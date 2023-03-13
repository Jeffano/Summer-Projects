import pathlib
import os
import pygame

inputdirectory = r'/Users/Jeffano/Desktop/TheBuckmasterInstitute/PythonVideoProjects/ReadPlayAudioFiles/Music/'

initial_count = 0
for path in pathlib.Path("/Users/Jeffano/Desktop/TheBuckmasterInstitute/PythonVideoProjects/ReadPlayAudioFiles/Music").iterdir():
    if path.is_file():
        initial_count += 1

print('\nThere are', initial_count, 'audio files\n')

list = os.listdir('/Users/Jeffano/Desktop/TheBuckmasterInstitute/PythonVideoProjects/ReadPlayAudioFiles/Music')
print(list)

song = input("\nEnter The Song File You Wish To Play: ")
file = os.path.join(inputdirectory, song)

pygame.init()
pygame.mixer.music.load(file)

while True:
    n = input("Type Play or Stop to start or stop the song. \nType Exit to stop the program:\n")
    if n == "play" :
        pygame.mixer.music.play()
    elif n == "stop":
        pygame.mixer.music.pause()
    elif n == "exit":
        exit()