#!/usr/bin/env python

from nltk.corpus import treebank
from os import path
import sys

output_dir = sys.argv[1]

for fileid in treebank.fileids():
    basename, _ = path.splitext(fileid)
    ann_filename = path.join(output_dir, '{}.ann'.format(basename))
    if path.isfile(ann_filename):
        output_filename = path.join(output_dir, '{}.txt').format(basename)
        with open(output_filename, 'w') as f:
            for sent in treebank.sents(fileids=[fileid]):
                words = [x for x in sent if not x.startswith('*') and x != '0']
                f.write(' '.join(words))
                f.write('\n')
