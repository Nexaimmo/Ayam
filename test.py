import time
import sys

def putar_lagu():
    lirik = [
        ('Now she got a six-year-old', 0.07),
        ('Trying to keep him warm', 0.06),
        ('Trying to keep out the cold', 0.07),
        ('When he looks her in the eyes', 0.06),
        ("He don't know he is safe when she says", 0.06),
        ("Ooh, love, no one's ever gonna hurt you, love", 0.07),
        ("I'm gonna give you all of my love", 0.07),
        ("Nobody matters like you", 0.11),
        ('So, rockabye, baby, rockabye', 0.10),
        ("I'm gonna rock you", 0.07),
        ("Rockabye, baby, don't you cry", 0.07),
        ("Somebody's got you", 0.07),
    ]

    delay = [0.1, 0.1, 0.1, 0.3, 0.1, 0.1, 0.1, 0.4, 0.4, 0.4, 0.4, 0.1]

    time.sleep(1)
    for i, (line_song, delay_character) in enumerate(lirik):
        for char in line_song:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(delay_character)
        time.sleep(delay[i % len(delay)])
        print('')

putar_lagu()
