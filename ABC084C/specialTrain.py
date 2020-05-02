import sys

print("Enter number of stations.")
N = int(input())
Clt = []
Slt = []
Flt = []
for i in range(1, N, 1):
    print("Enter time C, S, F of the station " + str(i) + ".")
    C, S, F = (int(x) for x in input().split())
    if S % F != 0:
        print("S must be diviible by F.")
        sys.exit()
    else:
        Clt.append(C)
        Slt.append(S)
        Flt.append(F)
Xlt = []
print(range(N-2))
for j in range(N-1):
    X = Slt[j] + Clt[j]
    for k in range(j+1, N-1, 1):
        if Slt[k] < X:
            X = X + ((X - Slt[k]) % Flt[k]) + Clt[k]
        else:
            X = X + (Slt[k] - X) + Clt[k]
    Xlt.append(X)
Xlt.append(0)
print("Output time X of each station.")
for l in range(N):
    print(Xlt[l])
