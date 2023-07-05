# Infinite breakcore

does what it says on the can

## Setup

1. Download and extract the code .zip at <https://github.com/Elijah/Tyler/Inifnite-breakcore.git>
2. Open Terminal in the project directory and type `python -m pip install -r requirements.txt`

### config.json

If you want to change the settings for the program, you can do so in the config.json file. The attributes are as follows:

- **bpm** - the tempo of the song
- **synth_phrase_length** - how often a new synth note is played
- **drum_phrase_length** - how often a new drum pattern is picked
- **drum_patterns** - list of drum patterns, see default for example
- **repeat_patterns** - whether or not the program will repeat the same drum pattern (only matters if drum_phrase_length is longer than the selected pattern)
- **include-silence** - whether or not the program will include silence as a randomly selected drum sound
- **pattern_weight** - likelihood of playing a drum pattern as opposed to random notes; 0 <= pattern_weight <= 1
- **drum_bank** - which folder to pull drum sounds from
- **synth_bank** - which folder to pull synth sounds from
- **warp_samples** - whether or not the drum samples get warped based on the bpm

## Run

`python main.py`

It's randomly generated breakcore, what's not to love?
