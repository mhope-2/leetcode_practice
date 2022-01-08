import math

def rev(s: str) -> str:
    if len(s) >=1 and len(s) <= math.pow(10, 4):
        l = s.strip().split()
        return " ".join(reversed(l))
    else:
        return

print(rev(" a good example "))