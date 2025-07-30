def minimum(a, x):
    r = a % x
    return min(r, (x - r) % x)
