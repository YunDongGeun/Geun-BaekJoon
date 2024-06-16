arr = []
while(True):
    a, b = map(int, input().split())
    if (a != 0 and b != 0):
        arr.append((a, b))
    else:
        break

for i in range(0, len(arr)):
    if(arr[i][0], arr[i][1] != 0):
        if (arr[i][0] > arr[i][1]):
            print("Yes")
        elif(arr[i][0] <= arr[i][1]):
            print("No")
