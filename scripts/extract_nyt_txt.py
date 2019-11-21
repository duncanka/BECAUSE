#!/usr/bin/env python
# Usage: extract_nyt.py OUTPUT_PATH [NYT_XML_FILE]...

from __future__ import print_function
from nltk.corpus.reader import XMLCorpusReader
import os
import sys
from subprocess import call


def make_body_extractor(kicker):
    if len(kicker) == 0:
        return lambda elt: '\n\n'.join([c.text for c in elt.getchildren()])
    else:
        kicker = kicker.__iter__().next()
        def extractor(elt):
            pars = [c.text for c in elt.getchildren()]
            if pars[-1].strip() == kicker:
                pars.pop()
            return '\n\n'.join(pars)
        return extractor

def make_attr_extractor(attr_name):
    return lambda elt: elt.get(attr_name)

text_extractor = lambda elt: elt.text
kicker_extractor = make_attr_extractor('series.name')

### Generic functions for running extractors on the document and handling the results ###

def extract_feature(doc, xpath, extractor=text_extractor):
    result = set()
    elts = doc.findall(xpath)
    for elt in elts:
        extracted = extractor(elt)
        if extracted is None:
            continue
        # Extractor can return multiple items. If it did, add them all.
        if hasattr(extracted, '__iter__'):
            result.update(extracted)
        else:
            result.add(extracted)

    return result

def add_features(name, doc_dict, values, max_allowed=1, required=True):
    if len(values) > max_allowed:
        raise ValueError(name)
    elif len(values) == 0:
        if required:
            raise ValueError(name)

    for i, value in enumerate(values):
        doc_dict[name + ("_%d" % i)] = value
    for i in range(len(values), max_allowed):
        doc_dict[name + ("_%d" % i)] = ''

### Driver ###

def process_doc(doc):
    doc_dict = {}
    kicker = extract_feature(doc, './/head/docdata/series', kicker_extractor)
    add_features('body', doc_dict,
                 extract_feature(doc, './/body/body.content/block[@class="full_text"]',
                                 make_body_extractor(kicker)))
    return doc_dict

def doc_path_to_dict(path):
    directory, fname = os.path.split(path)
    reader = XMLCorpusReader(directory, fname)
    doc = reader.xml()
    try:
        return process_doc(doc)
    except ValueError, e:
        return e.args[0]

def main(argv):
    if len(argv) < 3:
        print('Usage: extract_nyt.py OUTPUT_PATH [NYT_XML_FILE]...')
        exit(1)

    target_path = argv[1]
    file_paths = argv[2:]

    files_written = []

    for path in file_paths:
        doc_dict = doc_path_to_dict(path)
        _, filename = os.path.split(path)
        dir_path = target_path
        path_base = os.path.join(dir_path, os.path.splitext(filename)[0])
        files_written.append(path_base + '.txt')
        with open(files_written[-1], 'w') as txt_file:
            txt_file.write(doc_dict['body_0'].encode('utf-8'))

    if call('sed -i.bak -f quotes.sed'.split() + files_written) == 0:
        for f in files_written:
            os.remove(f + '.bak')
    else:
        print("Could not run sed. Please replace all initial quotes in text files with `` instead of ''.")

if __name__ == '__main__':
    main(sys.argv)
