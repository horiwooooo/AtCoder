import sys

print("Enter the number N of columns.")
N = int(input())
# make initial lists to store the number of candies in each column
A1 = []
A2 = []
# enter the number of candies in each row and column
print("Enter the numeber of candies in row 1.")
A1 = [int(a) for a in input().split()]
if len(A1) != N:
    print("Error!! Enter the number of candies for N columns.")
    sys.exit()
print("Enter the numeber of candies in row 2.")
A2 = [int(a) for a in input().split()]
if len(A2) != N:
    print("Error!! Enter the number of candies for N columns.")
    sys.exit()
max = 0
for i in range(N):
    tmp = sum(A1[0:i+1])+sum(A2[i:N])
    if max < tmp:
        max = tmp
print("The maximum number of candies is " + str(max) + " .")
