from StringIO import StringIO

import pytest

from flexrle import encode, decode


test_strings = ["", "a", "aa", "ab",
                "aabbaabbababaaabbbaaaabbbb",
                "\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff",
                "hello world",
                "a little bit longer test, with some punctuation!"]


@pytest.mark.parametrize('s', test_strings)
def test_encode_decode_round_trip(s):
    f_src = StringIO(s)
    f_encoded = StringIO()
    f_decoded = StringIO()
    encode(f_src, f_encoded)
    f_encoded.seek(0)
    decode(f_encoded, f_decoded)
    f_src.seek(0)
    f_decoded.seek(0)
    assert (f_src.read() == f_decoded.read())

