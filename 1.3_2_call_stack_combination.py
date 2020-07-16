# function of combination C[n][k]
n, k = map(int, input().split())

sz = max(n, k) + 1
c = [[0] * sz for x in range(sz)]

c[0][0] = 1
for i in range(1, sz):
    for j in range(i + 1):
        c[i][j] = c[i - 1][j] + c[i - 1][j - 1]

print(c[n][k])