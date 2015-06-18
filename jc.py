from math import floor
def unrank(N, K, r, perm):
        perm_index = [0] * K

        for k in range(0, K):
            perm_index[k] = int(r % (N-k))
            perm[k] = perm_index[k]
            for i in range(0, k):
                if perm_index[i] <= perm_index[k]:
                    perm[k] += 1
            r = floor(r/(N-k))

def rank(N, K, perm):
    r = perm[0]
    for k in range(1, K)[::-1]:
        q = perm[k]
        for i in range(0, k):
            if perm[i] < perm[k]:
                q -= 1
        r += q * fac[N]/fac[N-k]
    return r

def main():
	print 'Lehmer Code'

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
	for index in range(0, fac[N]/fac[N-K]):
		perm = [-1] * K
		unrank(N, K, index, perm)
		r = rank(N, K, perm)
		print index, '\t', perm, '\t', r

	print 'done'

if __name__ == "__main__":
    main()
