# BECauSE v0.5 Data Release

This directory includes the annotated data from version 0.5 of the **B**ank of **E**ffects and **Cau**ses **S**tated **E**xplicitly (BECauSE). This is the dataset reported on in Dunietz et al., 2017. The documents have all been exhaustively annotated using the scheme described in Dunietz et al., 2015. (The dataset is an expanded version of the one described in that paper.) All annotations are in `.ann` files formatted for <a href="http://brat.nlplab.org/">brat</a>, and we have included the `annotation.conf` and `visual.conf` files for brat in this directory.

There are three subdirectories, each containing data from a different source:

* **CongressionalHearings**: Three partial documents from the <a href="https://sites.google.com/site/unsharedtask2014/">2014 NLP Unshared Task in PoliInformatics</a>. These documents are freely available, but for ease of processing, some header information was stripped from the text files. We also annotated only portions of these files, not complete transcripts. To allow for others to use our annotation offsets, then, we have included the preprocessed text files alongside the annotations.

* **NYT**: 59 randomly selected documents from the year 2007 of the Washington section of the <a href="https://catalog.ldc.upenn.edu/ldc2008t19">New York Times Annotated Corpus</a> (Sandhaus, 2008). Each `.ann` file shares its name with the corresponding raw NYT article. An LDC subscription is required to obtain the raw files.

* **PTB**: 47 documents randomly selected from sections 2-23 of the Penn Treebank (Marcus et al., 1994). We excluded WSJ documents that were either earnings reports or corporate leadership/structure announcements, as both
tended to be merely short lists of names/numbers. Again, we provide offset annotations named to match the raw PTB files, but the raw files require an LDC subscription.

Note that we are currently working on an enhanced and further expanded version of this corpus. That version will include about 20% more documents, and the annotations will be made more consistent for treatment of edge cases. The future release will also include annotations for instances where causal language overlaps with about 8 different other types of relations. (These cases are not handled fully consistently in this release.)


#### Citations

<sub>Dunietz, Jesse, Lori Levin, and Jaime Carbonell. Automatically Tagging Constructions of Causation and Their Slot-Fillers. In press; to be published in 2017. *Transactions of the Association for Computational Linguistics*.</sub>

<sub>Dunietz, Jesse, Lori Levin, and Jaime Carbonell. Annotating Causal Language Using Corpus Lexicography of Constructions. *Proceedings of LAW IX – The 9th Linguistic Annotation Workshop* (2015): 188-196.</sub>

<sub>Sandhaus, Evan. 2008. The New York Times annotated corpus. *Linguistic Data Consortium*, Philadelphia.</sub>

<sub>Marcus, Mitchell, et al. 1994. The Penn Treebank: Annotating predicate argument structure. In *Proceedings of the Workshop on Human Language Technology*, HLT '94, pages 114-119. Association for Computational Linguistics, Stroudsburg, PA, USA.</sub>
