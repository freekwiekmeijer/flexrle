from struct import calcsize

preamble_fmt = ">H"
preamble_size = calcsize(preamble_fmt)

word_sizes = {i: 2**i for i in range(4)}

max_steps = 2**13 - 1
