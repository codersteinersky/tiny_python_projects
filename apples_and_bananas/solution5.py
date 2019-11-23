#!/usr/bin/env python3
"""Apples and Bananas"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='str',
                        type=str,
                        default='a',
                        choices=list('aeiou'))

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel

    # Method 5: Define a function, use list comprehension
    def new_char(c):
        return vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c

    text = ''.join([new_char(c) for c in text])

    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
