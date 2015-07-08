Terminator
==========


ARPA File Format
====


KenLM
====

**KenLM Installation**

```
wget -O - http://kheafield.com/code/kenlm.tar.gz |tar xz 
cd kenlm
./bjam -j4
```

**Train a Model**

```
bin/lmplz -o 5 <text >text.arpa
```

For more details, see https://kheafield.com/code/kenlm/ and https://github.com/alvations/usaarhat-repo/blob/master/Modelling-W-Ken.md
