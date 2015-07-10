
import io, sys
from collections import Counter

import kenlm

from extract import extract_line_by_line, extract_for_whole_file

from association_measures import lmpmi, lmpmi_freq
from filter import low_score_filter

'''    
model_file = '/home/alvas/test/food.arpa'
textfile = '/home/alvas/test/food.txt'
model = kenlm.LanguageModel(model_file)

for line, terms in extract_line_by_line(textfile, model):
    print '\t'.join([line, str(terms), str(low_score_filter(terms, 4.0))])

for term, score, count in extract_for_whole_file(textfile, model):
    print '\t'.join([term, score, count])
'''

def main(model_file, textfile):
    model = kenlm.LanguageModel(model_file)
    for term, score, count in extract_for_whole_file(textfile, model):
        print('\t'.join([term, str(score), str(count)]))
    
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
