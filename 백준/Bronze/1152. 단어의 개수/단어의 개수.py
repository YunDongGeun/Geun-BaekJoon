string = input()

cnt = 0
isWord = False
if (string != " "):
    for i in range(0, len(string) - 1):
        if (isWord == False and string[i].isalnum()):
            isWord = True
            cnt += 1
        elif (isWord == True and not string[i].isalnum()):
            isWord = False

    if (isWord == False):
        cnt += 1

print(cnt)
