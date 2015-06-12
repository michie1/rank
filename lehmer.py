from math import floor, factorial

fac = []

def nthTrue(S, n):
	j = -1 # first found is called the 0st # aantal true
	i = -1
	while j < n:
		i += 1
		if S[i]:
			j += 1

	S[i] = False
	return i
	#print i
	"""
	j = 0
	for i in range(0, len(S)):
		if S[i]:
			j += 1
			if j > n:
				S[i] = False
				return i
	"""

def unrank(N, K, r):
	S = [True] * N;
	n = N
	result = [-1] * K
	for k in range(0, K):
		result[k] = nthTrue(S, int(r % n))
		r = floor(r/n)
		n -= 1
	return result

def rank(N, K, perm):
	S = range(0, N)
	index = 0
	for k in range(0, K):
		"""
		i = 0
		j = 0
		while perm[k] != S[i]:
			if S[i] >= 0:
				j += 1
			i += 1
		#print j, perm[k], S[i]
		index += j * (fac[N]/fac[N-k])
		S[j] = -1
		"""
		
		for i, s in enumerate(S):
			if perm[k] == s:
				index += i * (fac[N]/fac[N-k])
				S.pop(i)
				break
	return index

def main():
	print 'Lehmer Code'

	N = 4
	K = 3

	fac.append(1)
	fac.append(1)
	for i in range(2, N+1):
		fac.append(i * fac[i-1]) 

	#print len(fac)
	#print fac[10]	


	#for index in range(0, factorial(N)/factorial(N-K)):
	for index in range(0, fac[N]/fac[N-K]):
	#for index in range(18, 19):
		perm = unrank(N, K, index)
		r = rank(N, K, perm)
		print index, '\t', perm, '\t', r
	#	if index != r:
		#	print index, '\t', perm, '\t', r
		#	break

	S = [1, 0, 0, 1, 1, 0, 1, 1]

	"""
	for i, b in enumerate(S):
		if b:
			aantal_true += 1
			if aantal_true == 2:
				print i
				break
	"""

	#print aantal_true

	print 
	print 'done'

if __name__ == "__main__":
    main()
