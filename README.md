Terminator
==========

Term Extraction using language model probabilities.


Usage
====

**Installation**

```
cd ~
# Install KenLM
wget -O - http://kheafield.com/code/kenlm.tar.gz |tar xz 
cd kenlm
./bjam -j4
cd ..
# Install KenLM python wrapper
pip install https://github.com/kpu/kenlm/archive/master.zip
# Install Terminator
git clone https://github.com/alvations/Terminator.git
```

**Usage**

```
cd Terminator
kenlm/bin/lmplz -o 5 < text.txt >text.arpa
python3 extract_terms.py text.arpa text.txt
```
