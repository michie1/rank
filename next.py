from math import floor 
factorial = [
   1,
   5,
   5*4,
   5*4*3,
   5*4*3*2,
]

def unrank(N, K, r, perm):
    perm_index = [0] * K
    
    #for k in range(0, K):
    for k in range(0, K):
        perm_index[k] = int(r % (N-k))
        r = floor(r/(N-k))

    for k in range(0, K):
        perm[k] = perm_index[k]
        i = k-1
        while i >= 0:
            if perm_index[i] <= perm[k]:
                perm[k] += 1
            i -= 1
    return perm_index

def rank(N, K, perm):
    #print perm
    r = perm[0]

    for k in range(1, K)[::-1]:
        q = perm[k]
        for i in range(0, k):
            if perm[i] < perm[k]:
                q -= 1
        r += q * factorial[k]
        #r += q * fac[N]/fac[N-k]
    return r

def next_rank(N, K, perm_index):
    #print perm_index, 
    perm_index[0] += 1
    if perm_index[0] == N:
        perm_index[0] = 0
        perm_index[1] += 1
        if perm_index[1] == N-1:
            perm_index[1] = 0
            perm_index[2] += 1
    """

    i = 0
    perm_index[0] += 1
    while perm_index[i] == N-i:
        perm_index[i] = 0
        perm_index[i+1]+= 1
    """


    perm = [0]*K
    for k in range(0, K):
        perm[k] = perm_index[k]
        i = k-1
        while i >= 0:
            if perm_index[i] <= perm[k]:
                perm[k] += 1
            i -= 1

    #print perm_index, perm
    #print perm
    return perm

def main():
    print 'Next ranking'

    N = 5 # Every digit in range [0, N-1]
    K = 3 # Permutation length

    # Precalculate faculty
    global fac
    fac = [0] * (N+1)
    fac[0] = 1
    fac[1] = 1
    for i in range(2, N+1):
        fac[i] = i * fac[i-1]


    # Loop thru all permutations and test rank/unrank
    perm = [0, 1, 2]
    perm_index = [0, 0, 0]
    for index in range(0, factorial[K]-1):
    #for index in range(0, 100):
    #for index in range(0, fac[N]/fac[N-K]-1):
        #perm_index = unrank(N, K, index, perm)
        print perm
        perm = next_rank(N, K, perm_index)
        #print perm, 
         
        """
        r = rank(N, K, perm)
        #print index, '\t', perm, '\t', r
        if index != r:
            print index, '\t', perm, '\t', r
            break
        if len(perm) != len(set(perm)):
            print index, '\t', perm, '\t', r
            break
        #print index, '\t', perm, '\t', r
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




    print 'done'

    #for s in range(0, 26):
    #    print s, skip_right[s], use_right[skip_right[s]]

if __name__ == "__main__":
    main()
