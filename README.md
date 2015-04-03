# flexrle.

Implements encoding and decoding functionality according to FlexRLE runlength coder.

## Data format

FlexRLE is a flexible runlength encoder which encodes sequences of identical words. Each word starts with a preamble, indicating the size of the following word and its number of repetitions.

The encoding of a word is as follows:
`
[p(2) w(1 ... 8)]
`
+ p: preamble (16 bits, Big-endian/NBO): `sssn nnnn  nnnn nnnn`
  - 3 bits (msb) indicating the size of the following word; size := 2^x
    - 0: 1 (int8)
    - 1: 2 (int16)
    - 2: 4 (int32)
    - 3: 8 (int64)
    - ...
  - 13 bits (lsb) indicating the number of repetitions
+ w: to-be-repeated data word, size in bytes according to the preamble


