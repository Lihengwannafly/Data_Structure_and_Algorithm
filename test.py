# string = raw_input()
string = "10+1 11+2"
attack, defense = string.split()
X, Y = attack.split("+")
H, D = defense.split("+")
X = int(X)
Y = int(Y)
H = int(H)
D = int(D)
count = 0

total = (D + 1) * (Y + 1)

if X >= H:
    if X >= (H + D):
        result = total

    else:
        result = total - (H + D - X) * (1 + H + D - X) // 2

else:
    if H > (X + Y):
        result = 0
    else:
        result = (X + Y - H + 1) * (1 + X + Y - H + 1) // 2

print(round(result / total, 2))
