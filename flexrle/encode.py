from operator import itemgetter
from struct import pack

from common import max_steps, preamble_fmt, word_sizes


def get_word(buf, pos, size):
    return (pos+size <= len(buf)) and buf[pos:pos+size] or None


def count_head(buf, pos, w):
    if not w:
        return 0
    initial_pos = pos
    size = len(w)
    steps = 0
    while (buf[pos:pos+size] == w) and (steps < max_steps):
        steps += 1
        pos += size
    return pos-initial_pos


def encode(buf):
    """Apply FlexRLE runlength encoding"""
    out = ''
    pos = 0
    while pos < len(buf):
        words = {b: get_word(buf, pos, s) for (b, s) in word_sizes.items()}
        head = {b: count_head(buf, pos, words[b]) for b in word_sizes}
        (code, jmp) = max(head.items(), key=itemgetter(1))
        word_size = word_sizes[code]
        out += pack(preamble_fmt, (code << 13) | ((jmp & 0xFFFF) >> code))
        out += buf[pos:pos+word_size]
        pos += jmp
    return out
