import json
import time
import random
import pygame
pygame.init()

with open("config.json") as f:
    config = json.load(f)

bpm = config["bpm"]
phrase_length = config["phrase_length"]
drum_patterns_temp = config["drum_patterns"]
drum_patterns = [0]*len(drum_patterns_temp)
for i in range(len(drum_patterns_temp)):
    drum_patterns[i] = drum_patterns_temp[str(i)]
random_weight = config["random_weight"]
pattern_weight = config["pattern_weight"]
drum_reset = config["drum_reset"]

drums_sound_list = [pygame.mixer.Sound(f"samples/{i}.wav") for i in range(1,9)]
drums_channel = pygame.mixer.Channel(1)
synth_sound_list = [pygame.mixer.Sound(f"samples/{i}.wav") for i in ['d','e','f','g','a']]
pad_channel = pygame.mixer.Channel(2)
pygame.mixer.init(int(44100*(bpm/137)))

def main():
    running = True
    while running:
        toggle = random.choices([0,1],[random_weight,pattern_weight])[0]

        if toggle:
            for i in range(phrase_length):
                if i == 0:
                    pad_channel.play(synth_sound_list[random.randint(0,len(synth_sound_list)-1)])
                drums_channel.play(drums_sound_list[random.randint(0,len(drums_sound_list)-1)])
                time.sleep(30/bpm)
        else:
            pattern_to_play = random.randint(0,len(drum_patterns)-1)
            for i in range(phrase_length):
                if i % 8 == 0: #TODO drum_reset: where does it go?
                    pattern_to_play = random.randint(0,len(drum_patterns)-1)
                if i == 0:
                    pad_channel.play(synth_sound_list[random.randint(0,len(synth_sound_list)-1)])
                drums_channel.play(drums_sound_list[drum_patterns[pattern_to_play][i % len(drum_patterns[pattern_to_play])]])
                time.sleep(30/bpm)

if __name__=="__main__":
    main()