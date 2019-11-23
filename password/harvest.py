#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-11-23
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import spacy


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='str',
                        type=str,
                        default='words')

    parser.add_argument('-l',
                        '--lower',
                        help='Lowercase output',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = spacy.load("en_core_web_sm")

    nouns, adjs, verbs = set(), set(), set()
    for fh in args.file:
        doc = nlp(fh.read())

        for token in doc:
            pos, word = token.pos_, token.lemma_

            if args.lower:
                word = word.lower()

            if pos == 'NOUN':
                nouns.add(word)
            elif pos == 'VERB':
                verbs.add(word)
            elif pos == 'ADJ':
                adjs.add(word)

    def write(words, name):
        if words:
            out_fh = open(os.path.join(out_dir, name), 'wt')
            out_fh.write('\n'.join(words))

    write(verbs, 'verbs.txt')
    write(nouns, 'nouns.txt')
    write(adjs, 'adjs.txt')

    total = sum(map(len, [verbs, adjs, nouns]))
    print(f'Done, wrote {total} to "{out_dir}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
