from collections import Counter

def f(s):
    r = {}
    for i in s:
        if i in r:
            r[i] += 1
        else:
            r[i] = 1
    return r

def f_alternative(s):
    return Counter(s)