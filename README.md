Terminator
==========

Term Extraction using language model probabilities.


Usage
====

```
git clone https://github.com/alvations/Terminator.git
cd Terminator
python3 extract_terms.py file.txt
```



KenLM
====

**KenLM Installation**

```
wget -O - http://kheafield.com/code/kenlm.tar.gz |tar xz 
cd kenlm
./bjam -j4
pip install https://github.com/kpu/kenlm/archive/master.zip
```

**Train a Model**

```
bin/lmplz -o 5 <text >text.arpa
```

For more details, see https://kheafield.com/code/kenlm/ and https://github.com/alvations/usaarhat-repo/blob/master/Modelling-W-Ken.md

**ARPA File Format**

See https://github.com/alvations/usaarhat-repo/blob/master/Know-ARPA.md and http://stackoverflow.com/questions/16408163/arpa-language-model-documentation for more information
