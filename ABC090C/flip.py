import sys

print("Enter the number of rows and columns.")
N, M = (int(a) for a in input().split())
if (not(isinstance(N, int))) or (not(isinstance(M, int))):
    print("Enter an integer.")
    sys.exit()
elif (N < 1) or (M < 1):
    print("Enter a value of 1 or more for the number N, M.")
    sys.exit()
elif (N > (10 ** 9)) or (M > (10 ** 9)):
    print("Enter a value of 1000000000 or less for the number N, M.")
    sys.exit()
# calculate the number of back cards
if (N > 2) and (M > 2):
    card = (N-2)*(M-2)
elif (N == 1) and (M == 1):
    card = 1
elif N == 1:
    card = M - 2
elif M == 1:
    card = N - 2
else:
    card = 0
print("The number of cards on the back is " + str(card) + ".")
