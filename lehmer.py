from math import floor

# find the m-th true boolean and return its index
def mthTrue(S, m):
	j = -1 # first found is called the 0st # aantal true
	i = -1
	while j < m:
		i += 1
		if S[i]:
			j += 1
			
	S[i] = False
	return i

# find index i and return which m-th true it is
# Assume S[i] is always True
def mthTrue_reverse(S, i):
	m = 0	# first found is called the 0st
	for j in range(0, i):
		if S[j]:
			m += 1

	S[i] = False
	return m

def unrank(N, K, r, perm):
	S = [True] * N;
	for k in range(0, K):
		perm[k] = mthTrue(S, int(r % (N-k)))
		r = floor(r/(N-k))

def rank(N, K, perm):
	S = [True] * N;
	r = 0
	for k in range(0, K):
		r += mthTrue_reverse(S, perm[k]) * (fac[N]/fac[N-k])

	return r

def main():
	print 'Lehmer Code'

	N = 4 # Every digit in range [0, N-1]
	K = 2 # Permutation length

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
