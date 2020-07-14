n = int(input()) # amount of elements input
if 1<=n<=100:
    i = 1
    x = 0 # default value
    while i <= n: 
        x += int(input()) # sum of values which depend of n 
        i += 1
    print(x)
     