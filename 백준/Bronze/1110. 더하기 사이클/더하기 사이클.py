i = 1
n = int(input())

def newN(n: int) -> int:
    e = n % 10
    f = n // 10
    return (e * 10 + (e + f) % 10)

num = newN(n)

while(n != num):
    num = newN(num)
    i += 1

print(i)