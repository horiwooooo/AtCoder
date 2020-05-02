print("Please enter the number of bills and the amount.")
N, Y = (int(x) for x in input().split())

# Linear Programming
for x in range(int((Y/1000 - N)//9 + 1)):
    for y in range(int((Y/1000 - N)//4 + 1)):
        z = N - x - y
        if (z >= 0) and (z == ((Y/1000)-(10*x)-(5*y))):
            print(str(x) + " " + str(y) + " " + str(z))
            break
        elif (x < int((Y/1000 - N)//9)) or (y < int((Y/1000 - N)//4)):
            continue
        else:
            print("-1 -1 -1")
    else:
        continue
    break

'''
# Model Answer
n, y = map(int, input().split())
for i in range(n + 1):
    for j in range(n - i + 1):
        if i * 10000 + j * 5000 + (n - i - j) * 1000 == y:
            print(i, j, n - i - j)
            exit()
print("-1 -1 -1")

'''
