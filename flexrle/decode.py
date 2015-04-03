from struct import unpack

from common import preamble_fmt, preamble_size, word_sizes


def decode(f_in, f_out):
    """Apply FlexRLE runlength decoding"""
    while True:
        p = f_in.read(preamble_size)
        if len(p) < preamble_size:
            break
        p = unpack(preamble_fmt, p)[0]
        code = (p & 0xE000) >> 13
        word_size = word_sizes[code]
        word_repetitions = p & 0x1FFF
        w = f_in.read(word_size)
        if len(w) < word_size:
            break
        for i in xrange(word_repetitions):
            f_out.write(w)
