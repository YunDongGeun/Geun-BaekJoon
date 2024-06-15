cnt = int(input())
words = []

for i in range(cnt):
    word = input()
    words.append(word)

words = list(set(words))
words.sort()
words.sort(key=len)

for i in range(0, len(words)):
    print(words[i])
