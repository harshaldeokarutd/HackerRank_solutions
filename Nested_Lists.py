output = []
test = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    abc = [name, score]
    output.append(abc)

y = [j for i in output for j in i if isinstance(j, float)]
y = list(dict.fromkeys(y))
x = sorted(y)
m = x[1]
print(m)
for k in output:
    if m in k:
        test.append(k[0])

test1 = sorted(test)
for h in test1:
    print(h)
