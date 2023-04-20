# import pygame
# import numpy as np

# # initialize pygame
# pygame.init()
# pygame.mixer.init()

# # set the sampling rate and duration
# # the sampling rate = how many different values per second of sound
# sampling_rate = 44100
# freq = 440.0 # Hz
# duration = 1.5 # seconds; duration of the sound sample

# # num of frames = vals per second * seconds in clip
# frames = int(sampling_rate * duration)
# arr = np.cos(2*np.pi*freq*np.linspace(0,duration,frames))
# buffer = np.asarray([32767*arr,32767*arr]).T.astype(np.int16)
# sound = pygame.mixer.Sound(buffer)
# # sound = pygame.sndarray.make_sound(sound.copy())
# sound.play()

import pygame
import numpy as np

pygame.mixer.init(size=32)

buffer = np.sin(2 * np.pi * np.arange(44100) * 440 / 44100).astype(np.float32)
sound = pygame.mixer.Sound(buffer)

sound.play(0)
pygame.time.wait(int(sound.get_length() * 1000))