  N = int(input())
# Lists in Python - Hacker Rank Solution START
test = [];
for i in range(0, N):
    ip = input().split()
    if ip[0] == "print":
        print(test)
    elif ip[0] == "insert":
        test.insert(int(ip[1]), int(ip[2]))
    elif ip[0] == "remove":
        test.remove(int(ip[1]))
    elif ip[0] == "pop":
        test.pop();
    elif ip[0] == "append":
        test.append(int(ip[1]))
    elif ip[0] == "sort":
        test.sort()
    else:
        test.reverse()
