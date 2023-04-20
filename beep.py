import winsound

freq = [400,500]
dur = 300

for f in freq:
    winsound.Beep(f, dur)