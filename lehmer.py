from math import floor, factorial

def unrank(N, K, index):
	S = range(0, N)
	n = N
	result = []
	for k in range(0, K):
		result.append(S.pop(int(index % n)))
		index = floor(index/n)
		n -= 1
	return result

def rank(N, K, perm):
	S = range(0, N)
        index = 0
	for k in range(0, K):
            for i, s in enumerate(S):
                if perm[k] == s:
                    index += i * (factorial(N)/factorial(N-k))
                    S.pop(i)
                    break
        return index

def main():
	print 'Lehmer Code'

	N = 47
	K = 5
	
	for index in range(0, factorial(N)/factorial(N-K)):
            perm = unrank(N, K, index)
            print index, '\t', perm, '\t',
            r = rank(N, K, perm)
            print r

if __name__ == "__main__":
    main()
