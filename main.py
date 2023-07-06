import os
import json
import time
import random
import pygame
pygame.init()

with open("config.json") as f:
    config = json.load(f)

synth_phrase_length = config["synth_phrase_length"]
drum_phrase_length = config["drum_phrase_length"]
drum_patterns = config["drum_patterns"]
repeat_patterns = config["repeat_patterns"]
include_silence = config["include_silence"]
pattern_weight = config["pattern_weight"]
drum_bank = f'samples/drum/{config["drum_bank"]}'
if not (bpm := config["bpm"]):
    with open(f"{drum_bank}/data.json") as f:
        bpm = json.load(f)["bpm"]
synth_bank = f'samples/synth/{config["synth_bank"]}'
if config["warp_samples"]:
    with open(f"{drum_bank}/data.json") as f:
        drum_bank_bpm = json.load(f)["bpm"]
    pygame.mixer.init(int(44100*(bpm/drum_bank_bpm))) # this doesn't actually work
else:
    pygame.mixer.init(44100)

drums_sound_list = [pygame.mixer.Sound(f"{drum_bank}/{i}") for i in os.listdir(drum_bank) if i[-4:] == ".wav"]
drums_channel = pygame.mixer.Channel(1)
synth_sound_list = [pygame.mixer.Sound(f"{synth_bank}/{i}") for i in os.listdir(synth_bank) if i[-4:] == ".wav"]
pad_channel = pygame.mixer.Channel(2)

def main():
    running = True
    beat = 0
    while running:
        if beat % synth_phrase_length == 0:
            pad_channel.play(synth_sound_list[random.randint(0,len(synth_sound_list)-1)])

        if beat % drum_phrase_length == 0:
            random_toggle = random.choices([0,1],[pattern_weight,1-pattern_weight])[0] # 0 = play from patterns, 1 = play random sample
            pattern_to_play = random.randint(0,len(drum_patterns)-1)
        note_to_play = random.randint(0 - include_silence,len(drums_sound_list)-1) if random_toggle else drum_patterns[pattern_to_play][beat % len(drum_patterns[pattern_to_play])]

        if note_to_play != -1:
            drums_channel.play(drums_sound_list[note_to_play])
        time.sleep(30/bpm)

        beat += 1

if __name__=="__main__":
    main()