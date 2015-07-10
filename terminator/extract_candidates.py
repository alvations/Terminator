
import io
from collections import Counter

import kenlm

from extract import extract_candidates_only

model_file = '/home/alvas/test/food.arpa'
textfile = '/home/alvas/test/food.txt'
model = kenlm.LanguageModel(model_file)

fout = io.open('food.candidates', 'w', encoding='utf8')
for text, candidates in extract_candidates_only(textfile, model):
     fout.write(text + '\t' + candidates + '\n')