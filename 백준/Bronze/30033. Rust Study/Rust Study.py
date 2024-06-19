num = int(input())

arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
cnt = 0

for i in range(num):
    if (arr[i] <= arr2[i]):
        cnt += 1
        
print(cnt) 