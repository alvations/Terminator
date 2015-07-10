
import io, sys, time
import operator
from collections import Counter
from itertools import chain

from association_measures import logprob, lmpmi, lmpmi_freq
from filter import noun_phrase_filter, simple_filter

def fame(textfile, model, measure=lmpmi):
    extracted_terms_counts = Counter()
    extracted_terms_measure = {}
    start = 0
    with io.open(textfile, 'r', encoding='utf8') as fin:
        for line_count, line in enumerate(fin):
            if line_count == 0 or line_count % 50 == 0:
                start = time.time()
                print line_count,
            if line_count != 0 and line_count % 500 == 0:
                print 'took', time.time() - start, 'secs'
                start = 0
                print
            noun_phrases = noun_phrase_filter(line)
            for ng in simple_filter(noun_phrases):
                if ng not in extracted_terms_measure:
                    score = measure(ng, model)
                    extracted_terms_measure[ng] =score
                else:
                     score = extracted_terms_measure[ng]
                if score !=0:
                    extracted_terms_counts[ng]+=1
    return extracted_terms_counts, extracted_terms_measure            
    
    

def lame(text, model, measure=lmpmi):
    ranked_term_candidates = {}
    noun_phrases = noun_phrase_filter(text)
    for ng in simple_filter(noun_phrases):
        score = measure(ng, model)
        if score != 0:
            ranked_term_candidates[ng] =  score
    return sorted(ranked_term_candidates.items(), key=operator.itemgetter(1), 
                  reverse=True)

def extract_line_by_line(textfile, model, method=lame):
    with io.open(textfile, 'r', encoding='utf8') as fin:
        for count, line in enumerate(fin):
            if line.strip():
                extracted_terms = method(line.strip(), model, measure=lmpmi)
                #y = lame(line.strip(), model, measure=lmpmi_freq)
                #fx = low_score_filter(x, 4.0)
                #fy = low_score_filter(y, 0.0001)
                yield line.strip(), extracted_terms
                
def extract_for_whole_file(textfile, model, method=fame):
    extracted_terms_counts, extracted_terms_measure  = method(textfile, model, measure=lmpmi)
    for ng in sorted(extracted_terms_counts):
        yield ng, extracted_terms_measure[ng], extracted_terms_counts[ng] 