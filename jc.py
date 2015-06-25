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


# unrank by rank
def unrank(N, K, r, perm):
    perm_index = [0] * K
    
    perm_index[0] = int(r % 26)
    r = floor(r/26)
    perm[0] = perm_index[0]
    perm[0] = skip_right[perm[0]]
    
    for k in range(1, K):
        perm_index[k] = int(r % (N-k))
        r = floor(r/(N-k))

    for k in range(1, K):
        perm[k] = perm_index[k]
        i = k-1
        while i >= 0:
            if perm_index[i] <= perm[k]:
                perm[k] += 1
            i -= 1
        perm[k] = skip_dens[perm[k]]

# unrank to index
#def unrank_to_index(N, K, r):


# rank by perm
def rank(N, K, perm):
    perm[0] = use_right[perm[0]]
    r = perm[0]
    for k in range(1, K):
        perm[k] = use_dens[perm[k]]

    for k in range(1, K)[::-1]:
        q = perm[k]
        for i in range(0, k):
            if perm[i] < perm[k]:
                q -= 1
        r += q * factorial[k]
    return r

# rank by index
def index_to_rank(N, K, perm_index):
    r = perm_index[0]
    for k in range(1, K): 
        r += perm_index[k] * factorial[k]
    return r

def rank_to_index(r, perm_index):
    perm_index[0] = int(r % 26)
    r = floor(r/26)

    for k in range(1, K):
        perm_index[k] = int(r % (47-k))
        r = floor(r / (47-k))

# next index
def increment_index(N, K, perm_index):
    # increment index
    """
    perm_index[0] += 1
    if perm_index[0] == 26:
        perm_index[0] = 0
        perm_index[1] += 1
    """
    if perm_index[0] < 25:
        perm_index[0] += 1
    else: # == 25
        perm_index[0] = 0
        perm_index[1] += 1

    i = 1
    while perm_index[i] == N-i:
        perm_index[i] = 0
        perm_index[i+1]+= 1
        i += 1

def index_to_perm(N, K, perm, perm_index):
    # Get perm by index
    for k in range(0, K):
        perm[k] = perm_index[k]
        i = k-1
        while i >= 0:
            if perm_index[i] <= perm[k]:
                perm[k] += 1
            i -= 1

    # transform to game
    perm[0] = skip_right[perm[0]]
    for k in range(1, K):
        perm[k] = skip_dens[perm[k]]

def perm_to_index(N, K, perm, perm_index):
    # transform from game
    perm_index[0] = use_right[perm[0]]
    for k in range(1, K):
        perm_index[k] = use_dens[perm[k]]
    
    #print perm
    #perm_index[0] = skip_right[perm[0]]
    #for k in range(1, K):
    #    perm_index[k] = skip_dens[perm[k]]

    # to index
    for k in range(0, K)[::-1]:
    #for k in range(1, K)[::-1]:
        i = k-1
        while i >= 0:
            if perm_index[k] > perm_index[i]:
                perm_index[k] -= 1
            i -= 1
        #perm_index[k] = use_dens[perm[k]]

def main():
    print 'Jungle Checkers ranking'

    global N, K
    N = 47 # Every digit in range [0, N-1]
    K = 3 # Permutation length

    # Precalculate faculty
    global fac
    fac = [0] * (N+1)
    fac[0] = 1
    fac[1] = 1
    for i in range(2, N+1):
        fac[i] = i * fac[i-1]


    bla = [43, 4, 0]
    #bla = [0, 1, 2]
    bla_index = [0, 0, 0]
    #perm_to_index(N, K, bla, bla_index)
    #print bla_index
    #perm_by_index(N, K, bla, bla_index)
    #print bla
    #print rank_by_index(N, K, bla_index)
    #print rank(N, K, bla)

    perm = range(0, K)
    perm_index = [0]*K
        
    # Loop thru all permutations and test rank/unrank
    #for index in range(0, factorial[K]-1):
    i = 0
    r = 0
    while i < factorial[K]-1:

    #while i < 100:
        r = index_to_rank(N, K, perm_index)
        if r != i:
            print r, i
            break
        increment_index(N, K, perm_index)

        
        #perm = [-1] * K
        
        #unrank(N, K, index, perm)

        #perm2 = perm[:]


        #r = rank(N, K, perm2) # this changes perm
        #perm2 = [0]*K 
        #perm_by_index(N, K, perm2, perm_index)
        

        #print i, perm2, perm_index, rank_by_index(N, K, perm_index), perm2, rank(N, K, perm2),

        #perm3 = perm[:]
        #next_index(N, K, perm_index)
        #perm3 = [0]*K
        #perm_by_index(N, K, perm3, perm_index)
        #print perm3
        

        #print perm, index, r, perm3
        i += 1
        #print perm 
        #print index, '\t', perm, '\t', r
        #if index != r:
        #    print index, '\t', perm, '\t', r
        #    break
        #print index, '\t', perm, '\t', r

    #print perm
    #print i, perm_index, rank_by_index(N, K, perm_index), perm2, rank(N, K, perm2),
    
    """
    bla = [1, 8, 10, 9]
    bla_index = [0, 0, 0, 0]
    index_by_perm(N, K, bla, bla_index)
    #print bla_index
    print rank_by_index(N, K, bla_index)
    perm_by_index(N, K, bla, bla_index)
    print bla
    print rank(N, K, bla)
    """

    """

    index = 1
    perm = [-1] * K
    unrank(N, K, index, perm)
    r = rank(N, K, perm)
    print index, '\t', perm, '\t', r
    
    index = 12
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


    perm = [42, 0, 4]
    perm_index = [0, 0, 0]
    perm_to_index(N, K, perm, perm_index)
    print perm_index
    index_to_perm(N, K, perm, perm_index)
    print perm
    print index_to_rank(N, K, perm_index)
    print rank(N, K, perm)
    unrank(N, K, 2416, perm)
    print perm
    print index_to_rank(N, K, perm_index)
    rank_to_index(2416, perm_index)
    print perm_index


    print 'done'

    #for s in range(0, 26):
    #    print s, skip_right[s], use_right[skip_right[s]]

if __name__ == "__main__":
    main()
