import winsound
import time

# define notes and their corresponding frequencies
NOTES = {'C': 262, 'D': 294, 'E': 330, 'F': 349, 'G': 392, 'A': 440, 'B': 494}

# example melody
twinkle_twinkle = [('C', 500), ('C', 500), ('G', 500), ('G', 500),
                   ('A', 500), ('A', 500), ('G', 1000),
                   ('F', 500), ('F', 500), ('E', 500), ('E', 500),
                   ('D', 500), ('D', 500), ('C', 1000)]

# define a function to play a note for a given duration
def play_note(note, duration):
    frequency = NOTES.get(note, 0)
    if frequency:
        winsound.Beep(frequency, duration)

# define a function to play a melody using a list of notes and durations
def play_melody(melody):
    for note, duration in melody:
        play_note(note, duration)
        time.sleep(duration / 1000)

# play the melody
play_melody(twinkle_twinkle)