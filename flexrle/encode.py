#!/usr/bin/env python

from operator import itemgetter
from os import SEEK_CUR
from struct import pack

from common import max_steps, preamble_fmt, word_sizes
from shell import run_from_shell


def get_words(f, sizes):
    initial_pos = f.tell()
    w = f.read(max(sizes))
    f.seek(initial_pos)
    return map(lambda s: len(w) >= s and w[:s] or None, sizes)


def count_head(f, w):
    if not w:
        return 0
    initial_pos = f.tell()
    size = len(w)
    steps = 0
    while (f.read(size) == w) and (steps < max_steps):
        steps += 1
    f.seek(initial_pos)
    return steps*size


def encode(f_in, f_out):
    """Apply FlexRLE runlength encoding"""
    while True:
        words = dict(zip(word_sizes.keys(),
                         get_words(f_in, word_sizes.values())))
        if words.values()[0] is None:
            break  # end of data: could not read the smallest sized word
        head = {code: count_head(f_in, words[code]) for code in word_sizes}
        (code, jmp) = max(head.items(), key=itemgetter(1))
        f_in.seek(jmp, SEEK_CUR)
        f_out.write(pack(preamble_fmt,
                         (code << 13) | ((jmp & 0xFFFF) >> code)))
        f_out.write(words[code])


if __name__ == "__main__":
    run_from_shell(encode)
