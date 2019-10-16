from convolution import Filter

MEAN = Filter(1, 1, [
    1, 1, 1,
    1, 1, 1,
    1, 1, 1
], 9)

GAUSSIAN = Filter(1, 1, [
    1, 2, 1,
    2, 4, 2,
    1, 2, 1
], 16)

LAPLACIAN1 = Filter(1, 1, [
     0, -1,  0,
    -1,  4, -1,
     0, -1,  0
], 1)

LAPLACIAN2 = Filter(1, 1, [
    -1, -1, -1,
    -1,  8, -1,
    -1, -1, -1
], 1)
