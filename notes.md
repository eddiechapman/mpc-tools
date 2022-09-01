# MPC Tools project

> Some ideas for programming solutions to MPC problems such as creating chromatic programs etc.

Make a website featuring multiple browser-based tools for converting, renaming samples, creating custom programs, playing back audio

## Tools ideas:

### rename files (16 character limit)

- https://medium.com/@aneel.kaushikk/bulk-rename-utility-redesign-a-ux-case-study-82269ad27205

what are the MPC filename limitations?
- 16 characters
- UTF-8? No weird characters?

columns:
- filename
- filename length
- file size
- audio length
- play
- new name
- errors

actions on selected filenames:
- find and replace
- lower
- upper
- append
- prepend
- number
- reset name

errors:
- filename too short (0)
- filename too long
- incompatible character found
- duplicate filename

favicon from https://www.reddit.com/r/mpcusers/comments/u2zhmj/mpc_pixel_art/

### convert samples (to 16 bit 44k wav)

### make chromatic/pitched pgm from one or more samples

## Resources

- [mingus](https://bspaans.github.io/python-mingus/) python music theory library
- [crepe](https://github.com/marl/crepe) for audio pitch detection


## Questions

**Limits on audio uploads?**

**How to detect pitch?**

- crepe library

**How to convert pitch from Hz to piano scale (eg. C3)?**

- [stackoverflow: Turning frequencies into notes in Python](https://stackoverflow.com/questions/64505024/turning-frequencies-into-notes-in-python)
- [`note_to_freq.py`](https://gist.github.com/CGrassin/26a1fdf4fc5de788da9b376ff717516e#file-note_to_freq-py)
- [John D. Cook: Musical pitch notation](https://www.johndcook.com/blog/2016/02/10/musical-pitch-notation/)


## Walkthrough

Example with one sample:

1. enter audio file
2. detect pitch in frequency (multi step)
3. convert pitch to note name
4. calculate how to tune the sample to fill in the whole scale

Example with multiple samples:

1. enter audio files
2. detect pitches
3. convert pitches to note names
4. fill in scale with samples evenly distributed
5. calculate pitch shifts for each note