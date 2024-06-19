t = int(input())

arr = []
for i in range(t):
    n, m = map(int, input().split())
    if (n >= 12 and m >= 4):
        arr.append(12*m - (m - 4))
    else:
        arr.append(-1)

for i in range(len(arr)):
    print(arr[i])