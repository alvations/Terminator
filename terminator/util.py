
from nltk.util import ngrams

def ngramize(text, min_n, max_n):
    return [" ".join(ng) for ng in 
            chain(*[ngrams(text.split(),n) for n in range(min_n,max_n+1)])]
