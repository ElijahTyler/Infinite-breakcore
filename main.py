import sys
import time
import random
import pygame
pygame.init()

headless = False
if len(sys.argv) > 1:
    if sys.argv[1] in ['-h', "--headless"]:
        headless = True

drums_bpm = 170
phrase_length = 16

drums_sound_list = [pygame.mixer.Sound(f"samples/{i}.wav") for i in range(1,9)]
synth_sound_list = [pygame.mixer.Sound(f"samples/{i}.wav") for i in ['d','e','f','g','a']]
drums_channel = pygame.mixer.Channel(1)
pad_channel = pygame.mixer.Channel(2)
pygame.mixer.init(int(44100*(drums_bpm/137)))

def main():
    if not headless:
        screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Definitely not a keygen")

    running = True
    beat = 0
    while running:
        if not headless:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            print(beat)
        if beat == 0:
            pad_channel.play(synth_sound_list[random.randint(0,len(synth_sound_list)-1)])

        drums_channel.play(drums_sound_list[random.randint(0,len(drums_sound_list)-1)])
        time.sleep(30/drums_bpm)
        beat = (beat + 1) % phrase_length

if __name__=="__main__":
    main()