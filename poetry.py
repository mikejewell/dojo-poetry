#!/usr/local/bin/python
import re
import sys

from random import choice, randint
RHYME = sys.argv[1].upper()

vowels = ['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW']
cons = ['B', 'CH', 'D', 'DH', 'F', 'G', 'HH', 'JH', 'K', 'L', 'M', 'N', 'NG', 'P', 'R', 'S', 'SH', 'T', 'TH', 'V', 'W', 'Y', 'Z', 'ZH']
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "V", "X", "Y", "Z"]
shakes_words_2 = ['thee', 'thy', 'thou', 'hast', 'doth', 'canst']

endings = {}
rhymes = {}
syls = {}
words = []
shakes_words = []
lines = []

# Build up the various hashmaps, syllable count, etc

f = open('dict', 'r')
dict_lines = f.readlines()

for line in dict_lines:
    line = line.strip()
    pieces = line.split(" ")

    word = pieces[0]
    word = re.sub(r'\([0-9]+\)', '', word)
    words.append(word)

    phonemes = pieces[2:]
    phon_list = []

    for phoneme in phonemes:
        new_phoneme = re.sub(r'[0-9]', '', phoneme)
        phon_list.append(new_phoneme)

    index = -1
    syl_count = 0
    for idx, phon in enumerate(phon_list):
        if phon in vowels:
            if idx > 0 and phon_list[idx-1] in cons:
                index = idx-1
                syl_count = syl_count + 1

    key = " ".join(phon_list[index:])
    endings[word] = key

    syls[word] = syl_count
    if syl_count % 2 == 0:
        # Even number of syllables counts as a 'shakespeare-ish word'
        shakes_words.append(word)

    if not key in rhymes:
        rhymes[key] = []
    if word not in rhymes[key]:
        rhymes[key].append(word)

## Construct the poetry!

ending = endings[RHYME]
rhyme_options = rhymes[ending]

for i in range(0, 2):
    lines.append([choice(rhyme_options)])

for j in range(2, 5):
    line = []
    for x in range(1, 3):
        line.append(choice(shakes_words))
        if randint(0, 5) < 2:
            line.append(choice(shakes_words_2))
    line.append(choice(rhyme_options))
    lines.append(line)

lines.append([choice(rhyme_options)])
lines.append([RHYME])

# First line becomes the title
print lines[0][0]
print "-"*len(lines[0][0])
print

# The rest get capitalised and printed out
for line in lines[1:]:
    print " ".join(line).capitalize()

# Add an author
print "\t\t--- "+choice(alpha).lower()+". "+choice(alpha).lower()+". "+choice(rhyme_options).lower()
