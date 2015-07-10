
import io, sys
import operator
from itertools import chain
from collections import Counter

import kenlm

from association_measures import pointwise_mutual_information as pmi
from association_measures import logprob, lmpmi, lmpmi_freq
from filter import noun_phrase_filter, simple_filter, low_score_filter
    
def lame(text, model, measure=lmpmi):
    ranked_term_candidates = {}
    noun_phrases = noun_phrase_filter(text)
    for ng in simple_filter(noun_phrases):
        score = measure(ng, model)
        if score != 0:
            ranked_term_candidates[ng] =  score
    return sorted(ranked_term_candidates.items(), key=operator.itemgetter(1), 
                  reverse=True)
    
model_file = '/home/alvas/test/food.arpa'
textfile = '/home/alvas/test/food.txt'
model = kenlm.LanguageModel(model_file)

terms2lmpmi = {}
extracted_terms = Counter()
with io.open(textfile, 'r', encoding='utf8') as fin:
    for count, line in enumerate(fin):
        if line.strip():
            print count, line.strip()
            x = lame(line.strip(), model, measure=lmpmi)
            y = lame(line.strip(), model, measure=lmpmi_freq)
            fx = low_score_filter(x, 4.0)
            fy = low_score_filter(y, 0.0001)
            extracted_terms.update(x)
            print x, '\n', y, '\n', fx, '\n', fy, '\n'

if __name__ == '__main__':
    RED, NATIVE = '\033[01;31m', '\033[m'
    def err_msg(txt):
        return RED + txt + NATIVE

    if len(sys.argv) is not 3:
        usage_msg = err_msg('Usage: python3 %s language_model textfile \n'
                            % sys.argv[0])

        example_msg = err_msg('Example: python3 %s food.arpa food.txt' 
                              % sys.argv[0])
        sys.stderr.write(usage_msg)
        sys.stderr.write(example_msg)
        sys.exit(1)

    main(*sys.argv[1:])
