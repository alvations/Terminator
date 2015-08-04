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
pip3 install https://github.com/kpu/kenlm/archive/master.zip
# Install NLTK
pip3 install numpy
pip3 install -U nltk
# Install Senna 
wget http://ronan.collobert.com/senna/senna-v3.0.tgz
tar zxvf senna-v3.0.tgz
# Install Terminator
git clone https://github.com/alvations/Terminator.git


```

**Extract**

```
# Download test data (Food related sentences from Wikipedia)
wget -O WIKI_food.txt https://db.tt/1PsHukOB 
cut -f2 WIKI_food.txt > food.txt 
~/kenlm/bin/lmplz -o 5 < food.txt > food.arpa
sed '1,500!d' food.txt > food.500.txt
python3 ~/Terminator/terminator/extract_terms.py food.arpa food.500.txt
```
