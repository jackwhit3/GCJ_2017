import sys
sys.setrecursionlimit(2000)
def simpleSolve(A, st, en, K, sym):
	symCount = 0
	for c in A[st:en]:
		if c == sym:
			symCount += 1
	if (symCount == 0):
		return 0
	elif (symCount == K):
		return 1
	return -1

def flipFromLast(A, st, en, K):
	a = list(A)
	for i in range(en-K, en):
		if i < 0:
			continue
		print i
		if a[i] == '+':
			a[i] = '-'
		else:
			a[i] = '+'
	print A
	print ''.join(a)
	return ''.join(a)

def f(A, st, en, K):
	print [A, st, en]
	N = len(A[st:en])
	if N == K:
		return simpleSolve(A, st, en, K, '-')

	lastCake = A[en-1]
	if lastCake == '-':
		AA = flipFromLast(A, st, en, K)
		subSol = f(AA, st, en-1, K)
		if subSol == -1:
			return -1
		return 1 + subSol
	else:
		subSol = f(A, st, en-1, K)
		if subSol == -1:
			return -1
		return subSol

fn = 'A-large-practice.in'
out = 'A-large-practice.out'
fp = open(fn, 'r')
fw = open(out, 'w')
T = int(fp.readline())

for i in range(0,T):
	line = fp.readline()
	args = line.split()
	A = args[0]
	K = int(args[1])
	dic = {}
	res = f(A, 0, len(A), K)
	if res == -1:
		res = 'IMPOSSIBLE'
	fw.write('Case #' + str(i+1) + ': ' + str(res) + '\n')
	print "=========================================="
