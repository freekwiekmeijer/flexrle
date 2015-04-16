# flexrle

Implements encoding and decoding functionality according to FlexRLE runlength coder.

## Data format

FlexRLE is a flexible runlength encoder which encodes sequences of identical words. Each word starts with a preamble, indicating the size of the following word and its number of repetitions.

The encoding of a word is as follows:
`
[p(2) w(1 ... 8)]
`
+ p: preamble (16 bits, Big-endian/NBO): `cccn nnnn  nnnn nnnn`
  - c: 3 bits (msb) indicating the size of the following word; size := 2^x
    - 0: 1 (int8)
    - 1: 2 (int16)
    - 2: 4 (int32)
    - 3: 8 (int64)
    - 4 ... 6: reserved for future use
    - 7: raw sequence (indicates nr bytes to follow)
  - n: 13 bits (lsb) indicating the number of repetitions
+ w: to-be-repeated data word, size in bytes according to the preamble

## Usage

+ As python module:

```
>>> from flexrle import encode, decode
>>> encode(open("source_file", "rb"), open("compressed_file.rle", "w+b"))
>>> decode(open("compressed_file.rle", "rb"), open("uncompressed_file", "w+b"))
```

+ From command line:
```
$ python flexrle/encode.py source_file compressed_file.rle
$ python flexrle/decode.py compressed_file.rle uncompressed_file
```

## Current limitations

+ Encoder does not implement anything beyond a simple local optimization.
