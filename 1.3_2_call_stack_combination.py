# function of combination C[n][k]
# variant 1
n, k = map(int, input().split())

sz = max(n, k) + 1
c = [[0] * sz for x in range(sz)]

c[0][0] = 1
for i in range(1, sz):
    for j in range(i + 1):
        c[i][j] = c[i - 1][j] + c[i - 1][j - 1]

print(c[n][k])

# variant 2
def f(x):
	if x == 0:
		return 1
	return f(x-1) * x

def C(n,k):
	if k == 0:
		return 1
	elif k > n:
		return 0
	r = f(n)/(f(n-k)*f(k))
	return int(r)
n, k = map(int, input().split())


print(C(n,k))
