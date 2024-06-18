num = int(input())

n1 = 1
n2 = 1

if (num == 2):
    print("1/2")
elif (num == 3):
    print("2/1")
else:
    for i in range(1, num):
        if ((n1 + n2) % 2 == 0):
            if (n1 != 1):
                n1 -= 1
            n2 += 1
        else:
            if (n2 != 1):
                n2 -= 1
            n1 += 1
            
    print(f"{n1}/{n2}")