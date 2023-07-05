import os
import json
import time
import random
import pygame
pygame.init()

with open("config.json") as f:
    config = json.load(f)

bpm = config["bpm"]
synth_phrase_length = config["synth_phrase_length"]
drum_phrase_length = config["drum_phrase_length"]
drum_patterns_temp = config["drum_patterns"]
drum_patterns = [None]*len(drum_patterns_temp)
for i in range(len(drum_patterns_temp)):
    drum_patterns[i] = drum_patterns_temp[str(i)]
pattern_weight = config["pattern_weight"]
drum_bank = f'samples/drum/{config["drum_bank"]}'
synth_bank = f'samples/synth/{config["synth_bank"]}'
if config["warp_samples"]:
    pygame.mixer.init(int(44100*(bpm/137)))
else:
    pygame.mixer.init(44100)

drums_sound_list = [pygame.mixer.Sound(f"{drum_bank}/{i}") for i in os.listdir(drum_bank)]
drums_channel = pygame.mixer.Channel(1)
synth_sound_list = [pygame.mixer.Sound(f"{synth_bank}/{i}") for i in os.listdir(synth_bank)]
pad_channel = pygame.mixer.Channel(2)

def main():
    running = True
    beat = 0
    while running:
        if beat % synth_phrase_length == 0:
            pad_channel.play(synth_sound_list[random.randint(0,len(synth_sound_list)-1)])

        if beat % drum_phrase_length == 0:
            toggle = random.choices([0,1],[pattern_weight,1-pattern_weight])[0]
            pattern_to_play = random.randint(0,len(drum_patterns)-1)
        if toggle:
            drums_channel.play(drums_sound_list[random.randint(0,len(drums_sound_list)-1)])
        else:
            drums_channel.play(drums_sound_list[drum_patterns[pattern_to_play][beat % len(drum_patterns[pattern_to_play])]])
        time.sleep(30/bpm)

        beat += 1

if __name__=="__main__":
    main()