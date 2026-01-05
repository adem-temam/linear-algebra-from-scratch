import math

def add(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must be the same length")
    return [v1[i] + v2[i] for i in range(len(v1))]


def subtract(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must be the same length")
    return [v1[i] - v2[i] for i in range(len(v1))]


def scalar_multiply(scalar, v):
    return [scalar * x for x in v]


def dot(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must be the same length")
    return sum(v1[i] * v2[i] for i in range(len(v1)))


def magnitude(v):
    return math.sqrt(dot(v, v))
