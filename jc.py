from math import floor

factorial = [
   1,
   26,
   1196,
   53820, # 26 * 46!/(46-3+1)!
   2368080,
   101827440,
   4276752480,
   175346851680
]
"""
factorial = [
    1,
    47,
    2162,
    97290,
    4280760,
    184072680,
    7731052560,
    316973154960
]
"""

skip_right = [
    0,   1,  2,
    6,   7,  8,  9,
    13, 14, 15, 16,
    20, 21, 22, 23,
    27, 28, 29, 30,
    34, 35, 36, 37,
    41, 42, 43
]

use_right = [
     0,  1,  2, -1, -1, -1, #-1?
     3,  4,  5,  6, -1, -1, -1,
     7,  8,  9, 10, -1, -1, -1,
    11, 12, 13, 14, -1, -1, -1,
    15, 16, 17, 18, -1, -1, -1,
    19, 20, 21, 22, -1, -1, -1,
    23, 24, 25    
]

skip_dens = [
     0,  1,  2,      4,  5,  6,
     7,  8,  9, 10, 11, 12, 13,
    14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27,
    28, 29, 30, 31, 32, 33, 34,
    35, 36, 37, 38, 39, 40, 41, 
    42, 43, 44,     46, 47, 48
]

use_dens = [
     0,  1,  2, -1,  3,  4,  5,
     6,  7,  8,  9, 10, 11, 12,
    13, 14, 15, 16, 17, 18, 19,
    20, 21, 22, 23, 24, 25, 26,
    27, 28, 29, 30, 31, 32, 33,
    34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, -1, 44, 45, 46
]


def unrank(N, K, r, perm):
    perm_index = [0] * K
    
    perm_index[0] = int(r % 26)
    r = floor(r/26)
    perm[0] = perm_index[0]
    perm[0] = skip_right[perm[0]]
    
    for k in range(1, K):
        perm_index[k] = int(r % (N-k))
        perm[k] = perm_index[k]
        for i in range(0, k):
            if perm_index[i] <= perm_index[k]:
                perm[k] += 1
        r = floor(r/(N-k))


def rank(N, K, perm):
    #r = use_right[perm[0]]
    perm[0] = use_right[perm[0]]
    r = perm[0]
    for k in range(1, K)[::-1]:
        q = perm[k]
        for i in range(0, k):
            if perm[i] < perm[k]:
                q -= 1
        r += q * factorial[k]
        #r += use_dens[q] * factorial[k]
    return r

def main():
    print 'Jungle Checkers ranking'

    N = 47 # Every digit in range [0, N-1]
    K = 3 # Permutation length

    # Loop thru all permutations and test rank/unrank
    for index in range(0, factorial[K]-1):
            perm = [-1] * K
            unrank(N, K, index, perm)
            r = rank(N, K, perm)
            if index != r:
                print index, '\t', perm, '\t', r
    """
    index = 51
    perm = [-1] * K
    unrank(N, K, index, perm)
    r = rank(N, K, perm)
    print index, '\t', perm, '\t', r
    
    index = 52
    perm = [-1] * K
    unrank(N, K, index, perm)
    r = rank(N, K, perm)
    print index, '\t', perm, '\t', r

    index = factorial[K]-1
    perm = [-1] * K
    unrank(N, K, index, perm)
    r = rank(N, K, perm)
    print index, '\t', perm, '\t', r
    """



    print 'done'

    #for s in range(0, 26):
    #    print s, skip_right[s], use_right[skip_right[s]]

if __name__ == "__main__":
    main()
