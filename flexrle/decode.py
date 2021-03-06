#!/usr/bin/env python

from struct import unpack

from common import preamble_fmt, preamble_size, word_sizes
from shell import run_from_shell


def decode(f_in, f_out):
    """Apply FlexRLE runlength decoding"""
    while True:
        p = f_in.read(preamble_size)
        if len(p) < preamble_size:
            break
        p = unpack(preamble_fmt, p)[0]
        code = (p & 0xE000) >> 13

        if code == 7:
            # special case: raw data, n bytes
            word_size = word_repetitions
            word_repetitions = 1
        else:
            # default case: word size = 2^c, repetitions = n
            word_size = word_sizes[code]
            word_repetitions = p & 0x1FFF

        w = f_in.read(word_size)
        if len(w) < word_size:
            break
        for i in xrange(word_repetitions):
            f_out.write(w)


if __name__ == "__main__":
    run_from_shell(decode)
