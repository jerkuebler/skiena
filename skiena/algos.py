def knapsack(setn, num):
    """O(n) implementation of knapsack algo, takes largest to smallest nums"""
    i = 0
    answer = []
    maxn = 0
    setn = sorted(setn)

    while i < num:
        maxn = setn[-1]
        if maxn <= (num - i):
            i += maxn
            setn.remove(maxn)
            answer.append(maxn)
        else:
            setn.remove(maxn)

    return answer

def long_seq(sequence, best=''):
    for item in sequence:
        best = best[best.find(item) + 1:] + item
        yield best