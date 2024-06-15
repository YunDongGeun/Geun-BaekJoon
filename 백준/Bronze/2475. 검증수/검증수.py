arr = input().split()

numbers = [int(num) for num in arr]
result = 0

for i in numbers:
    result += i ** 2

print(result % 10)