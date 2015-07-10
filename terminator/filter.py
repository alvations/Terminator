
from os.path import expanduser
from string import punctuation

from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize
from nltk.tag.senna import SennaTagger, SennaChunkTagger

chktagger = SennaChunkTagger(expanduser("~")+'/senna')
STOPWORDS = stopwords.words('english')

def simple_filter(list_of_ngrams):
    return [ng for ng in list_of_ngrams if 
            ng.lower() not in STOPWORDS and
            ng[0] not in punctuation and ng[-1] not in punctuation and
            ng.split()[-1].lower() not in STOPWORDS and
            ng.split()[0].lower() not in STOPWORDS and
            not any(i for i in ng.split() if i.lower() in STOPWORDS) and
            any(pos for word,pos in pos_tag(ng.lower().split()) 
                if pos.startswith('NN')) and
            ')' not in ng and '(' not in ng and ',' not in ng and
            'pinyin' not in ng and 
            ng.split()[0] not in ['more', 'less']]

def noun_final_filter(list_of_ngrams):
    return [ng for ng in list_of_ngrams if
            pos_tag(word_tokenize(ng.lower()))[-1][1].startswith('NN')]

def remove_determiners(text):
    if text.lower().startswith(('a ', 'an ', 'the ')):
        text = " ".join(text.split()[1:])
    return text

def bio_to_chunk(bio_tagged_sent):
    np_chunks = []
    current_chunk = []
    for word, pos in bio_tagged_sent:
        if '-NP' in pos:
            current_chunk.append((word))
        else:
            if current_chunk:
                ng = remove_determiners(' '.join(current_chunk))
                np_chunks.append(ng)
                current_chunk = []            
    return np_chunks

def noun_phrase_filter(text):
    return bio_to_chunk(chktagger.tag(text.split()))

def low_score_filter(list_of_ngrams_and_prob, min_score):
    return [(ng,prob) for ng,prob in list_of_ngrams_and_prob if prob > min_score]