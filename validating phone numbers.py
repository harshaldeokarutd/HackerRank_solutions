import re

n = int(input())

for n in range(n):
    number = input()

    numbert = str(number)
    j = 0
    for i in numbert:
        j = j + 1

    if j == 10:
        x = re.search(r"^[789]\d{9}$", numbert)
        if x:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
