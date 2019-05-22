string = raw_input()
attack, defense = string.split()
X, Y = attack.split("+")
H, D = defense.split("+")
X = int(X)
Y = int(Y)
H = int(H)
D = int(D)
count = 0
for y in range(Y+1):
    for d in range(D+1):
        if y >= H-X+d:
            count += 1
print round(count / (Y+1) / (D+1), 2)