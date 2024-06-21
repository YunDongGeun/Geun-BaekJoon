bnp = list(map(int, input().split()))

if (bnp[1] >= bnp[2]):
    print(-1)
else:
    b = bnp[2] - bnp[1]
    print(bnp[0] // b + 1)
