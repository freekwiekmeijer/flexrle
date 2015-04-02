import pytest
from flexrle import encode, decode

test_strings = ["", "a", "aa", "ab", "hello world", "a little bit longer test, with some punctuation!"]


@pytest.mark.parametrize('s', test_strings)
def test_encode_decode_round_trip(s):
    assert decode(encode(s)) == s

