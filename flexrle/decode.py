from struct import unpack

from common import preamble_fmt, preamble_size, word_sizes


def decode(buf):
    """Apply FlexRLE runlength decoding"""
    out = ''
    pos = 0
    while True:
        p = buf[pos:pos+2]
        pos += preamble_size
        if len(p) < preamble_size:
            break
        p = unpack(preamble_fmt, p)[0]
        code = (p & 0xE000) >> 13
        word_size = word_sizes[code]
        word_repetitions = p & 0x1FFF
        w = buf[pos:pos+word_size]
        pos += word_size
        if len(w) < word_size:
            break
        out += w*word_repetitions
    return out
