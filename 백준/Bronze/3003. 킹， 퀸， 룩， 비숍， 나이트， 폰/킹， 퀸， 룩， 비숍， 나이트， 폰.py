arr = input().split()

numbers = [int(num) for num in arr]
chess = [1, 1, 2, 2, 2, 8]
string = ""

for i in range(0, len(numbers)):
    string += str(chess[i] - numbers[i]) + " "

print(string)