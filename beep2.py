import winsound

freq = 500
dur = 300

# winsound.Beep(freq, dur)
notes = {"A":220,
         "B":247,
         "C":261,
         "D":294,
         "E":329,
         "F":349,
         "G":392}


inp = input("What is the melody? ")
for letter in inp:
    winsound.Beep(notes[letter], 200)
