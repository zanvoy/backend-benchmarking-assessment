#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" anagrams
    Command line interface that accepts a word file and returns a dictionary of
    anagrams for that file.

    Module provides a function find_anagrams which can be used to do the same
    for an arbitrary list of strings.

"""
__author__ = "michael gabbard"

import sys


def alphabetize(string):
    return "".join(sorted(string.lower()))


def find_anagrams(words):
    anagrams = {}
    for word in words:
        if alphabetize(word) not in anagrams:
            anagrams[word] = [alphabetize(word)]
        else:
            anagrams[alphabetize(word)].append(word)
    return anagrams


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify a word file!")
        sys.exit(1)
    else:
        with open(sys.argv[1], 'r') as handle:
            words = handle.read().split()
            print(find_anagrams(words))
