import math

def solution(brown, yellow):
    for a in range(1, int(math.sqrt(yellow)) + 1):
        if yellow % a == 0:
            b = yellow // a
            if 2 * a + 2 * b + 4 == brown:
                return [b + 2, a + 2]