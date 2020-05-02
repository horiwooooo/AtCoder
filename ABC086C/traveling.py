print("Enter the number N.")
N = int(input())
# make lists of x,y
tLt = []
xLt = []
yLt = []
# enter t,x,y for each i
for i in range(1, N+1, 1):
    print("Enter t, x, y when i = " + str(i))
    t, x, y = (int(a) for a in input().split())
    tLt.append(t)
    xLt.append(x)
    yLt.append(y)
# make initial x,y
ti = 0
xi = 0
yi = 0
# verify the validity of coordinates x,y at time t at each i
for i in range(N):
    dif = (tLt[i]-ti) - (abs(xi-xLt[i])+abs(yi-yLt[i]))
    if (dif >= 0) and ((dif % 2) == 0):
        ti = tLt[i]
        xi = xLt[i]
        yi = yLt[i]
    else:
        print("No")
        break
else:
    print("Yes")
