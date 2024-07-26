num = int(input())
numbers = list(map(int, input().split()))[:num]
cnt = 0

def count_factors(n: int) -> int:
    n = abs(n)
    if n == 0 or n == 1:
        return 0
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count

for number in numbers:
    if count_factors(number) == 2:
        cnt += 1

print(cnt)
