# BECauSE v1.0 Data Release

This directory contains the annotated data from version 1.0 of the **B**ank of **E**ffects and **Cau**ses **S**tated **E**xplicitly (BECauSE). This is the dataset reported on in [Dunietz et al., 2017](http://www.cs.cmu.edu/~jdunietz/publications/causeway-system.pdf). The documents have all been exhaustively annotated using the scheme described in [Dunietz et al., 2015](http://www.cs.cmu.edu/~jdunietz/publications/causal-language-annotation.pdf). The dataset is an expanded version of the one described in the 2015 paper.

The corpus is an attempt to capture the enormous variety of constructions used to express cause and effect. Inspired by the principles of [Construction Grammar](https://en.wikipedia.org/wiki/Construction_grammar), we annotate any conventional pattern that expresses causation, however complex. BECauSE thus includes many constructions that are not annotatable in most schemes, and is more comprehensive than previous efforts to capture causal language. For details, see the aforementioned papers.

The list of causal constructions is available in the [constructicon](https://docs.google.com/spreadsheets/d/1xn-bEE76RNpdJdylmbQi81D8qPhpOxdIh61twTM-ycU/edit) used by annotators for this release.

All annotations are in `.ann` files formatted for [brat](http://brat.nlplab.org/), and we have included the `annotation.conf` and `visual.conf` files for brat in this directory. There are three data subdirectories, each containing data from a different source:

* **CongressionalHearings**: Three partial documents from the [2014 NLP Unshared Task in PoliInformatics](https://sites.google.com/site/unsharedtask2014/). These documents are freely available, but for ease of processing, some header information was stripped from the text files. We also annotated only portions of these files, not complete transcripts. To allow for others to use our annotation offsets, then, we have included the preprocessed text files alongside the annotations.

* **NYT**: 59 randomly selected documents from the year 2007 of the Washington section of the [New York Times Annotated Corpus](https://catalog.ldc.upenn.edu/ldc2008t19) (Sandhaus, 2008). Each `.ann` file shares its name with the corresponding raw NYT article. An LDC subscription is required to obtain the raw files.

  To turn the raw XML into the plain text files that the annotation offsets correspond to, you will need to run [`extract_nyt_txt.py`](scripts/extract_nyt_txt.py) on a system with access to `sed`. The script depends on NLTK.

* **PTB**: 47 documents randomly selected from sections 2-23 of the Penn Treebank (Marcus et al., 1994). We excluded WSJ documents that were either earnings reports or corporate leadership/structure announcements, as both
tended to be merely short lists of names/numbers. Again, we provide offset annotations named to match the raw PTB files, but the raw files require an LDC subscription.

  To turn the PTB `.mrg` files into the plain text files that the annotation offsets correspond to, you will need to run [`extract_wsj_txt.py`](scripts/extract_wsj_txt.py). The script depends on NLTK.

Note that there is an enhanced and further expanded version of this corpus, available from the master branch of this repository. That version includes about 20% more documents, and the annotations are more consistent for treatment of edge cases. That release also includes annotations for instances where causal language overlaps with about 7 different other types of relations. (These cases are not handled fully consistently in the 1.0 release.)


#### Citations

<sub>Dunietz, Jesse, Lori Levin, and Jaime Carbonell. Automatically Tagging Constructions of Causation and Their Slot-Fillers. In press; to be published in 2017. *Transactions of the Association for Computational Linguistics*.</sub>

<sub>Dunietz, Jesse, Lori Levin, and Jaime Carbonell. Annotating Causal Language Using Corpus Lexicography of Constructions. *Proceedings of LAW IX – The 9th Linguistic Annotation Workshop* (2015): 188-196.</sub>

<sub>Sandhaus, Evan. 2008. The New York Times annotated corpus. *Linguistic Data Consortium*, Philadelphia.</sub>

<sub>Marcus, Mitchell, et al. 1994. The Penn Treebank: Annotating predicate argument structure. In *Proceedings of the Workshop on Human Language Technology*, HLT '94, pages 114-119. Association for Computational Linguistics, Stroudsburg, PA, USA.</sub>
